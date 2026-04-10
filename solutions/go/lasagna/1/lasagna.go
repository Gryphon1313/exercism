package lasagna

const OvenTime = 40

// RemainingOvenTime returns the remaining minutes based on the `actual` minutes already in the oven.
func RemainingOvenTime(actualMinutesInOven int) int {
	if actualMinutesInOven >= 0 {
		var remaining = OvenTime - actualMinutesInOven
		if remaining <= 0 {
			return 0
		}
		return remaining
	}
	// error case passed a negative number
	return -1
}

// PreparationTime calculates the time needed to prepare the lasagna based on the amount of layers.
func PreparationTime(numberOfLayers int) int {
	if numberOfLayers >= 0 {
		return 2 * numberOfLayers
	}
	// error case as a negative number was passed
	return -1
}

// ElapsedTime calculates the time elapsed cooking the lasagna. This time includes the preparation time and the time the lasagna is baking in the oven.
func ElapsedTime(numberOfLayers, actualMinutesInOven int) int {
	if actualMinutesInOven >= 0 {
		return PreparationTime(numberOfLayers) + actualMinutesInOven
	}
	// error case as negative time in oven passed
	return -1
}
