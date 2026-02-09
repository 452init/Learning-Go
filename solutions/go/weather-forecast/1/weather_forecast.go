// Package weather provides tools for checking weather patterns.
package weather

var (
    // CurrentCondition stores current weather condition.
	CurrentCondition string
    // CurrentLocation stores location of the place.
	CurrentLocation  string
)
// Forecast is a function that returns the current
// state of weather of the current location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
