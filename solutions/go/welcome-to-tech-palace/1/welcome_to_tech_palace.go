package techpalace

import "strings"

// WelcomeMessage returns a welcome message for the customer.
func WelcomeMessage(customer string) string {
	var welcome_message string = "Welcome to the Tech Palace, "
	welcome_message += strings.ToUpper(customer)
	return welcome_message
}

// AddBorder adds a border to a welcome message.
func AddBorder(welcomeMsg string, numStarsPerLine int) string {
	var welcome_message string
	welcome_message = strings.Repeat("*", numStarsPerLine)
	welcome_message += "\n" + welcomeMsg + "\n"
	welcome_message += strings.Repeat("*", numStarsPerLine)
	return welcome_message
}

// CleanupMessage cleans up an old marketing message.
func CleanupMessage(oldMsg string) string {
	var cleaned_message string
	cleaned_message = strings.Replace(oldMsg, "*", "", -1)
	cleaned_message = strings.TrimSpace(cleaned_message)
	return cleaned_message
}
