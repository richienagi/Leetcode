nums = [-1, 0, 1, 2, -1, -4]
tripletList = []
cleanedTripletList = []

for i in range(0,len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[i] + nums[j] + nums[k] == 0:
                singleList = [nums[i],nums[j],nums[k]]
                tripletList.append(singleList)

for i in range(0,len(tripletList)):
    tripletList[i].sort()
    
cleanedTripletList.append(tripletList[0])
for i in range(0,len(tripletList)):
    if tripletList[i] not in cleanedTripletList:
        cleanedTripletList.append(tripletList[i])
