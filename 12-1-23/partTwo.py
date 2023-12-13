import regex as re

file = open("input.txt", "r")
numbers = []
sum = 0
for line in file:
    numbers = re.findall("0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True)
    for i in range(0, len(numbers)):
        if numbers[i] == "one":
            numbers[i] = "1"
        if numbers[i] == "two":
            numbers[i] = "2"
        if numbers[i] == "three":
            numbers[i] = "3"
        if numbers[i] == "four":
            numbers[i] = "4"
        if numbers[i] == "five":
            numbers[i] = "5"
        if numbers[i] == "six":
            numbers[i] = "6"
        if numbers[i] == "seven":
            numbers[i] = "7"
        if numbers[i] == "eight":
            numbers[i] = "8"
        if numbers[i] == "nine":
            numbers[i] = "9"
    first = int(numbers[0])
    last = int(numbers[len(numbers) - 1])
    newNum = (first * 10) + last
    sum += newNum
print(sum)