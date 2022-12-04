f = open("./input.txt", "r")
lines = f.readlines()

fullOverlaps = 0
partialOverlaps = 0  
for line in lines:
    ranges = line.strip().split(",")

    #The value of Discrete Mathematics lessons
    firstSet = set(range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1])+1))
    secondSet = set(range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1])+1))
    intersection = firstSet.intersection(secondSet)
    
    if(intersection==firstSet or intersection==secondSet):
        fullOverlaps+=1
        partialOverlaps+=1
    else: 
        if(len(intersection)!=0):
            partialOverlaps+=1

print("Solution 1:",fullOverlaps)
print("Solution 2:",partialOverlaps)
