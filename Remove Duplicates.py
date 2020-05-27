
# Remove Duplicates from Array (separate array)

test = [1,1,2,4,4,4]
output = []

for i in range(0,len(test)):
    if i == 0:
        output.append(test[i])
    else:
        count = 0
        for j in range(0,len(output)):
            if output[j] == test[i]:
                count = count + 1
        if count == 0:
            output.append(test[i])
            
