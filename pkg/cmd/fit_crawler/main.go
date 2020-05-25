package main

import (
	"encoding/json"
	"fmt"
	"time"

	"github.com/kelseyhightower/envconfig"

	"owm/io"
	"owm/objects"
)


type CrawlerConfig struct {
	ApiKey            string `default:""`
	SourceTag         string `default:"owm"`
	ClientTag         string `default:"server-ubuntu"`
	InfluxDBHost      string `default:"server"`
	InfluxDBPort      string `default:"12086"`
	InfluxDBUserName  string `default:"root"`
	InfluxDBPassword  string `default:"root"`
	InfluxDBDatabase  string `default:"smarthome"`
	ReadPeriodSeconds int    `default:"600"`
	Location          string `default:"Glover Park"`
}

func main() {
	var cfg CrawlerConfig
	err := envconfig.Process("", &cfg)
	if err != nil {
		fmt.Println(err)
		return
	}

	out, _ := json.MarshalIndent(cfg, "", "\t")
	fmt.Println(string(out))

	tags := objects.NewApiTags(cfg.SourceTag, cfg.ClientTag)

	location, ok := objects.Locations[cfg.Location]
	if !ok {
		fmt.Println(fmt.Sprintf("failed to load location [%v]", cfg.Location))
		return
	}

	period := time.Second * time.Duration(cfg.ReadPeriodSeconds)
	reader := io.NewOwmReader(cfg.ApiKey, location, tags)
	writer := io.NewDataWriter(cfg.InfluxDBHost, cfg.InfluxDBPort, cfg.InfluxDBUserName, cfg.InfluxDBPassword, cfg.InfluxDBDatabase)
	for {
		measurements := reader.Read()
		for _, m := range measurements {
			fmt.Println(fmt.Sprintf("type: %v - value: %v - dt : %v", m.Measurement(), m.Fields(), m.Timepoint()))
		}
		writer.Write(measurements)
		time.Sleep(period)
	}
}
