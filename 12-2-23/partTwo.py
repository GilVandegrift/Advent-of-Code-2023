'''
Advent of Code Day Two, part two
Gilbert Vandegrift
Goal: Given list of games with random amount of colored balls in the bag, and random amount shown.
Find the power of the set of minimum balls for each game and sum them
'''
import re

file = open("input.txt", "r")
powerSum = 0
for line in file:
    gameNum = re.findall("Game [0-9]+", line)
    redList = re.findall("[0-9]+ red", line)
    greenList = re.findall("[0-9]+ green", line)
    blueList = re.findall("[0-9]+ blue", line)
    
    minRed = 0
    minGreen = 0
    minBlue = 0
    numOfRed = []
    numOfGreen = []
    numOfBlue = []

    for red in redList:
        numOfRed.append(int(re.findall("[0-9]+", red)[0]))
    for green in greenList:
        numOfGreen.append(int(re.findall("[0-9]+", green)[0]))
    for blue in blueList:
        numOfBlue.append(int(re.findall("[0-9]+", blue)[0]))

    minRed = max(numOfRed)
    minGreen = max(numOfGreen)
    minBlue = max(numOfBlue)
    power = minRed * minGreen * minBlue
    powerSum += power

print(powerSum)