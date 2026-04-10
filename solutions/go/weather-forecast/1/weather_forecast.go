// Package weather provies the necessary tools for forcasting the weather in a given city.
package weather

var (
	// CurrentCondition represents the current weather for the set location.
	CurrentCondition string
	// CurrentLocation represents the location for which to forcast the weather for.
	CurrentLocation  string
)

// Forecast takes in two strings, city location and weather condition respectively. It will then
// return a string value detailing the weather for the provided inputs.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
