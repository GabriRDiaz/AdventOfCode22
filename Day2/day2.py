f = open("./input.txt", "r")
lines = f.readlines()

#Yes, yes... I could have computed it dynamically so it´s scalable. But I´m kinda lazy, you know :p
possiblePlay = {
    "AX": 4,
    "AY": 8,
    "AZ": 3,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 7,
    "CY": 2,
    "CZ": 6,
}

resultPerPlay = {
    "AX": 3,
    "AY": 4,
    "AZ": 8,
    "BX": 1,
    "BY": 5,
    "BZ": 9,
    "CX": 2,
    "CY": 6,
    "CZ": 7,
}

totalScore = 0
totalScorePerPlay = 0
for line in lines:
    totalScore+= possiblePlay[line.replace(" ","").strip()]
    totalScorePerPlay+= resultPerPlay[line.replace(" ","").strip()]
    
print("Solution 1:",totalScore)
print("Solution 2:",totalScorePerPlay)