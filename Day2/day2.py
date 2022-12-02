f = open("./input.txt", "r")
lines = f.readlines()

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

totalScore = 0
for line in lines:
    totalScore+= possiblePlay[line.replace(" ","").strip()]

print(totalScore)