package raindrops

import "fmt"

func Convert(number int) string {
	var convert_result string = ""
	if number%3 == 0 {
		convert_result += "Pling"
	}
	if number%5 == 0 {
		convert_result += "Plang"
	}
	if number%7 == 0 {
		convert_result += "Plong"
	}
	if convert_result == "" {
		convert_result = fmt.Sprint(number)
	}
	return convert_result
}
