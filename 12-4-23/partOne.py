import re

file = open("input.txt", "r")
score = 0
lineNum = 0
for line in file:
    lineNum += 1
    count = -1
    winAndGuess = line.split("|")
    winningNums = re.findall("[0-9]+", winAndGuess[0])
    guessedNums = re.findall("[0-9]+", winAndGuess[1])
    for num in guessedNums:
        if num in winningNums:
            count += 1
    if count == -1:
        continue
    curScore = 2**count
    print(lineNum)
    print(curScore)
    score += curScore

print(score)