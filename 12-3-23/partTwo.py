'''
Advent of Code Day 3, Part Two
Gilbert Vandegrift
Any * adjacent to exactly two parts is a gear, gear ratio is the two numbers multiplied together
sum all the gear ratios
'''

import re
nonSymbols = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

file = open("input.txt", "r")
engine = []
for line in file:
    engine.append(line)
    
sum = 0
for i in range(0, len(engine)):
    possibleGears = re.finditer("\*", engine[i])
    for gear in possibleGears:
        contact = 0

        location = gear.start()
        contactingParts = []

        PartsOne = re.finditer("[0-9]+", engine[i-1])
        PartsTwo = re.finditer("[0-9]+", engine[i])
        PartsThree = re.finditer("[0-9]+", engine[i+1])
        for part in PartsOne:
            start = part.start()-1
            end = part.end()+1
            theRange = range(start, end)
            if location in theRange:
                contactingParts.append(part.group())
                contact += 1
        for part in PartsTwo:
            start = part.start()-1
            end = part.end()+1
            theRange = range(start, end)
            if location in theRange:
                contactingParts.append(part.group())
                contact += 1
        for part in PartsThree:
            start = part.start()-1
            end = part.end()+1
            theRange = range(start, end)
            if location in theRange:
                contactingParts.append(part.group())
                contact += 1

        if contact == 2:
            gearRatio = int(contactingParts[0]) * int(contactingParts[1])
            sum += gearRatio
        else:
            print(location, i)
print(sum)