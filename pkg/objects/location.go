package objects

import (
	"fmt"
	owm "github.com/briandowns/openweathermap"
)

var (
	GLOVER_PARK = NewLocation(
		38.9225,
		-77.04,
	).WithName("Glover Park")

	AUSTIN = NewLocation(
		30.268871,
		-97.750713,
	).WithName("Austin")


	Locations = map[string]*Location{
		GLOVER_PARK.name: GLOVER_PARK,
		AUSTIN.name: AUSTIN,
	}
)

type Location struct {
	Lat  float64
	Lon  float64
	name string
}

func NewLocation(lat float64, lon float64) *Location {
	return &Location{
		Lat:  lat,
		Lon:  lon,
		name: fmt.Sprintf("%.4f,%.4f", lat, lon),
	}
}

func (l *Location) Area() string {
	return l.name
}

func (l *Location) WithName(name string) *Location {
	l.name = name
	return l
}

func (l *Location) Coordinates() *owm.Coordinates {
	return &owm.Coordinates{
		Longitude: l.Lon,
		Latitude:  l.Lat,
	}
}
