# Move Zeros - Brute Force
 
inputArray = [0,1,0,3,12]
outputArray = []
zeroCount = 0

for i in range(0,len(inputArray)):
    if inputArray[i] != 0:
        outputArray.append(inputArray[i])
    else:
        zeroCount = zeroCount + 1

for j in range(0,zeroCount):
    outputArray.append(0)
###########################################################
# No additional array
inputArray = [0,1,0,3,12]
zeroCount = inputArray.count(0)

for i in range(0,zeroCount):
    inputArray.remove(0)
    inputArray.append(0)
