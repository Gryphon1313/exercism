package partyrobot

import "fmt"

// Welcome greets a person by name.
func Welcome(name string) string {
	var message string = fmt.Sprintf("Welcome to my party, %s!", name)
	return message
}

// HappyBirthday wishes happy birthday to the birthday person and exclaims their age.
func HappyBirthday(name string, age int) string {
	var message string = fmt.Sprintf("Happy birthday %s! You are now %d years old!", name, age)
	return message
}

// AssignTable assigns a table to each guest.
func AssignTable(name string, table int, neighbor, direction string, distance float64) string {
	var message string
	message = Welcome(name)
	message += fmt.Sprintf("\nYou have been assigned to table %.3d. Your table is %s, exactly %.1f meters from here.", table, direction, distance)
	message += fmt.Sprintf("\nYou will be sitting next to %s.", neighbor)
	return message
}
