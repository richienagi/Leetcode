# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

test = [4,1,2,1,2]
duplicateArray = []

for i in range(0,len(test)):
    for j in range(0,len(test)):
        if test[j] == test[i] and i!=j:
            duplicateArray.append(test[j])

singleNumber = list(set(test)-set(duplicateArray))
print(singleNumber[0])
