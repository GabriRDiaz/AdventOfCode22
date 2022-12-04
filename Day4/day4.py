f = open("./input.txt", "r")
lines = f.readlines()

fullOverlaps = 0
partialOverlaps = 0  
for line in lines:
    ranges = line.strip().split(",")
    firstNumbers = ranges[0].split("-")
    secondNumbers = ranges[1].split("-")

    if((int(firstNumbers[0])<=int(secondNumbers[0]) and int(firstNumbers[1])>=int(secondNumbers[1]))
    or (int(secondNumbers[0])<=int(firstNumbers[0]) and int(secondNumbers[1])>=int(firstNumbers[1]))):
        fullOverlaps+=1
        partialOverlaps+=1
    else: 
        firstSet = set(range(int(firstNumbers[0]), int(firstNumbers[1])+1))
        secondSet = set(range(int(secondNumbers[0]), int(secondNumbers[1])+1))
        if(len(firstSet.intersection(secondSet))!=0): #The value of Discrete Mathematics lessons
            partialOverlaps+=1

print("Solution 1:",fullOverlaps)
print("Solution 2:",partialOverlaps)
