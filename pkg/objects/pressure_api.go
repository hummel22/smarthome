package objects

import "time"

type ApiPressure struct {
	Pressure float64
	Time     time.Time
	tags     Tags
}

func NewApiPressure(pressureC float64,
	t time.Time,
	tags Tags) *ApiPressure {
	return &ApiPressure{
		Pressure: pressureC,
		Time:     t,
		tags:     tags,
	}
}

func (a ApiPressure) Tags() Tags {
	return a.tags

}

func (a ApiPressure) Fields() Fields {
	return Fields{
		"value": float64(a.Pressure),
	}
}

func (a ApiPressure) Timepoint() time.Time {
	return a.Time
}

func (a ApiPressure) Measurement() string {
	return PRESSURE
}
