package objects

import "time"

type ApiTemperature struct {
	TemperatureC float64
	Time         time.Time
	tags     Tags
}

func NewApiTemperature(temperatureC float64,
	t time.Time,
	tags Tags) *ApiTemperature {
	return &ApiTemperature{
		TemperatureC: temperatureC,
		Time:         t,
		tags: tags,
	}
}

func (a ApiTemperature) Tags() Tags {
	return a.tags

}

func (a ApiTemperature) Fields() Fields {
	return Fields{
		"value": a.TemperatureC,
	}
}

func (a ApiTemperature) Timepoint() time.Time {
	return a.Time
}

func (a ApiTemperature) Measurement() string {
	return TEMPERATURE
}
