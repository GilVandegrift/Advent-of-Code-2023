'''
Advent of Code Day Two
Gilbert Vandegrift
Goal: Given list of games with random amount of colored balls in the bag, and random amount shown.
Identify and sum the game numbers of each game where it is possible to have
ONLY 12 red cubes, 13 green cubes, and 14 blue cubes
'''
import re

REDCUBES = 12
GREENCUBES = 13
BLUECUBES = 14

file = open("input.txt", "r")
gameSum = 0
for line in file:
    gameNum = re.findall("Game [0-9]+", line)
    redList = re.findall("[0-9]+ red", line)
    greenList = re.findall("[0-9]+ green", line)
    blueList = re.findall("[0-9]+ blue", line)
    tooMany = False

    for red in redList:
        numOfRed = int(re.findall("[0-9]+", red)[0])
        if numOfRed > REDCUBES:
            tooMany = True
            break
    for green in greenList:
        numOfGreen = int(re.findall("[0-9]+", green)[0])
        if numOfGreen > GREENCUBES:
            tooMany = True
            break
    for blue in blueList:
        numOfBlue = int(re.findall("[0-9]+", blue)[0])
        if numOfBlue > BLUECUBES:
            tooMany = True
            break
    if not(tooMany):
        increment = int(re.findall("[0-9]+", gameNum[0])[0])
        gameSum += increment

print(gameSum)
    