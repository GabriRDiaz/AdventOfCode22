f = open("input.txt", "r")
lines = f.readlines()
caloriesPerElf= {}
currentCalories=0

i=0
for line in lines:
    if(line=='\n'):
        caloriesPerElf[i]=currentCalories
        currentCalories = 0
        i+=1
    else:
        currentCalories+=int(line)

print("Solution 1:",max(caloriesPerElf.values()))

sortedCalories = sorted(caloriesPerElf.values(),reverse=True)
topThree = sortedCalories[0]+sortedCalories[1]+sortedCalories[2]

print("Solution 2:",topThree)