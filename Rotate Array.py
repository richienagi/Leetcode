# Rotate Array

test = [-1,-100,3,99]
out =[]
k = 1

for i in range(0,k):
    out.insert(0,test[len(test)-1-i])

test = test[:len(test)-k]
test = out+test
