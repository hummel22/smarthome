package io

import (
	"fmt"
	owm "github.com/briandowns/openweathermap"
	"time"

	"owm/objects"
)

type OwmReader struct {
	ApiKey   string
	Location *objects.Location
	tags     *objects.ApiTags
}

func NewOwmReader(apiKey string, location *objects.Location, tags *objects.ApiTags) *OwmReader {
	return &OwmReader{
		ApiKey:   apiKey,
		Location: location,
		tags:     tags,
	}
}

func (o *OwmReader) Read() []objects.Measurement {
	w, err := owm.NewCurrent("C", "EN", o.ApiKey)
	if err != nil {
		fmt.Println(fmt.Sprintf("failed to create owm current error: [%v]", err))
		return nil
	}

	err = w.CurrentByCoordinates(o.Location.Coordinates())
	if err != nil {
		fmt.Println(fmt.Sprintf("failed to read current by coordinates error: [%v]", err))
		return nil
	}

	// out, _ := json.MarshalIndent(w, "", "\t")
	// fmt.Println(string(out))

	timepoint := time.Unix(int64(w.Dt), 0)
	tags := o.tags.Tags(o.Location.Area())
	temp := objects.NewApiTemperature(w.Main.Temp, timepoint, tags)
	humidity := objects.NewApiHumidity(w.Main.Humidity, timepoint, tags)
	pressure := objects.NewApiPressure(w.Main.Pressure, timepoint, tags)

	return []objects.Measurement{temp, humidity, pressure}
}
