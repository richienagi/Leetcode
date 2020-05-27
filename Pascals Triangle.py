# Pascal's Triangle

numRows = 6
triangleArray = []
triangleArray2 = []

for i in range(0,numRows):
    if i == 0:
        triangleArray.append(1)
        print(triangleArray)
    elif i == 1:
        triangleArray.append(1)
        print(triangleArray)
    else:
        for j in range(0,len(triangleArray)-1):
            triangleArray2.append(triangleArray[j]+triangleArray[j+1])
        triangleArray2.insert(0,1)
        triangleArray2.append(1)
        print(triangleArray2)
        triangleArray = triangleArray2
        triangleArray2 = []
