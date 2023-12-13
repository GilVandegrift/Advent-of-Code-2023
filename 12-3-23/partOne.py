'''
Advent of Code Day 3, Part One
Gilbert Vandegrift
Any number adjacent to a symbol is an engine part - "." does not count as a symbol
Sum all the engine parts
'''

import re
nonSymbols = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

file = open("input.txt", "r")
engine = []
for line in file:
    engine.append(line)
    
sum = 0
for i in range(0, len(engine)):
    possibleParts = re.finditer("[0-9]+", engine[i])
    for part in possibleParts:
        contact = False
        start = part.start()
        if start != 0:
            start -= 1
        end = part.end()
        if end != 140:
            end += 1
        number = int(part.group())
        # print(part.start(), part.end(), part.group())#end is one past the last occupied index

        for j in range(start, end):
            if not(engine[i-1][j] in nonSymbols) or not(engine[i][j] in nonSymbols):
                contact = True
            if i != len(engine) - 1:
                if not(engine[i+1][j] in nonSymbols):
                    contact = True

        if contact:
            print(number)
            sum += number
print(sum)