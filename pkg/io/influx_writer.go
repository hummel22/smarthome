package io

import (
	"context"
	"fmt"
	"github.com/influxdata/influxdb-client-go"

	"owm/objects"
)

type DataWriter struct {
	client   influxdb2.Client
	database string
}

func NewDataWriter(host, port string, userName, password string, database string) *DataWriter {
	url := fmt.Sprintf("http://%v:%v", host, port)
	client := influxdb2.NewClient(url, fmt.Sprintf("%s:%s", userName, password))
	return &DataWriter{
		client:   client,
		database: database,
	}
}

func (db *DataWriter) Write(measurements []objects.Measurement) {
	for _, m := range measurements {
		writeApi := db.client.WriteApiBlocking("", db.database)
		p := influxdb2.NewPoint(
			m.Measurement(),
			m.Tags(),
			m.Fields(),
			m.Timepoint())
		// write synchronously
		err := writeApi.WritePoint(context.Background(), p)
		if err != nil {
			fmt.Println(fmt.Sprintf("failed to writer point err:[%v]", err))
		}
	}
}
