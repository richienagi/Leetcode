# Does Array contain duplicates?

test = [1,2,3,0]
duplicatePresent = False

for i in range(0,len(test)):
    for j in range(0,len(test)):
        if test[i] == test[j] and i !=j:
            duplicatePresent = True
