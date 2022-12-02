package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

/**
 * Day 1: Calorie Counting
 * https://adventofcode.com/2022/day/1
 **/

func main() {
	var fileName string = "data.txt"

	dataFile, err := os.Open(fileName)
	if err != nil {
		fmt.Println(err)
	}
	defer dataFile.Close()

	fileScanner := bufio.NewScanner(dataFile)
	fileScanner.Split(bufio.ScanLines)

	sum := 0
	maxSum := 0

	sumList := []int{}

	// Find largest sum for each group of numbers, return maxsum
	for fileScanner.Scan() {
		line := fileScanner.Text()

		if len(line) == 0 || line == "" {
			if sum > maxSum {
				maxSum = sum
			}
			sumList = append(sumList, sum)
			sum = 0
		} else {
			num, _ := strconv.Atoi(line)
			sum += num
		}

	}
	sort.Ints(sumList)
	fmt.Printf("Max Calories: %d\n", maxSum)

	// Print max 3
	topThreeSum := 0
	x := 0
	for i := len(sumList) - 1; i >= 0 && x < 3; i-- {
		topThreeSum += sumList[i]
		x++
	}
	fmt.Printf("Top Three Sum: %d\n", topThreeSum)
}
