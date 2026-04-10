package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	// need to treat the success rate as a percentage
	return float64(productionRate) * successRate / 100
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	return int(CalculateWorkingCarsPerHour(productionRate, successRate)) / 60
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	// batches of 10 cars can be produced for 95K
	// individual cars can be produced for 10K
	const cost_for_batch int = 95000
	const cost_per_car int = 10000
	var number_of_batches int = carsCount / 10
	var number_of_singles int = carsCount % 10

	return uint(cost_for_batch * number_of_batches + cost_per_car * number_of_singles)
}
