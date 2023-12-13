import re

file = open("input.txt", "r")
numbers = []
sum = 0
for line in file:
    numbers = re.findall("[0-9]", line)
    first = int(numbers[0])
    last = int(numbers[len(numbers) - 1])
    newNum = (first * 10) + last
    sum += newNum
print(sum)