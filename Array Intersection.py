 
 # Intersection of two arrays
 
nums1 = [1,2,2,1]
nums2 = [2]

set1 = set(nums1)
set2 = set(nums2)

a = list(set1.intersection(set2))
b = []
for i in range(0,len(a)):
    instances = min(nums1.count(a[i]),nums2.count(a[i]))
    for j in range(0,instances):
        b.append(a[i])
