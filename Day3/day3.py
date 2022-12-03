import string

def getRucksacksPriority(lines,alphabet):
    totalPriority=0
    for line in lines:
        splittedString = [line[:len(line)//2],line[len(line)//2:].strip()]
        for i in splittedString[0]:
            if(getDuplicated(i,splittedString)):
                totalPriority+=alphabet.index(i)+1
                break
    return totalPriority

def getGroupPriority(lines,alphabet):
    
    groupsPriority = 0
    groupString = []
    for i, line in enumerate(lines, start=1):
        groupString.append(line.strip())
        if(i%3==0):
            groupsPriority+=alphabet.index(getDuplicatedInGroup(i,groupString))+1
            groupString = []

    return groupsPriority    

def getDuplicatedInGroup(i,groupString):
    for element in groupString:
        for i in groupString[0]:
            for j in groupString[1]:
                if(i==j):
                    for k in groupString[2]:
                        if(i==k):
                            return i

def getDuplicated(i,splittedString):
    for j in splittedString[1]:
            if(i==j):
                return True

alphabet = list(string.ascii_lowercase+string.ascii_uppercase)

f = open("./input.txt", "r")
lines = f.readlines()
        
print("Solution 1:",getRucksacksPriority(lines,alphabet))
print("Solution 2:",getGroupPriority(lines,alphabet))
