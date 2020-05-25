package objects

import "time"

const (
	TEMPERATURE = "temperature"
	PRESSURE    = "pressure"
	HUMIDITY    = "humidity"
)

type Measurement interface {
	Tags() Tags
	Fields() Fields
	Timepoint() time.Time
	Measurement() string
}
