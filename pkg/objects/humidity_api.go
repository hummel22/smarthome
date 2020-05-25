package objects

import "time"

type ApiHumidity struct {
	Humidity int
	Time     time.Time
	tags Tags
}

func NewApiHumidity(humidity int,
	t time.Time,
	tags Tags) *ApiHumidity {
	return &ApiHumidity{
		Humidity: humidity,
		Time:     t,
		tags: tags,
	}
}

func (a ApiHumidity) Tags() Tags {
	return a.tags

}

func (a ApiHumidity) Fields() Fields {
	return Fields{
		"value": float64(a.Humidity),
	}
}

func (a ApiHumidity) Timepoint() time.Time {
	return a.Time
}

func (a ApiHumidity) Measurement() string {
	return HUMIDITY
}
