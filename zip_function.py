"""Multiple List using the zip function"""

l1 = [1,2,3]
l2 = [4,5,6,7,8]

for a,b in zip(l1,l2):
    # print(a, end= " ")
    # print(b, end= " ")
    if(a>b):
        print(a)
    else:
        print(b)
