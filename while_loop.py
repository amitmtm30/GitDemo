"""Execute statements repeatedly
conditions are used to stop the execution of loops
Iterable items are String, List, Tupple, Dictionary
"""
x=0
print(x)
while x<10:
    print("The value of x is " + str(x))
    x = x + 1
"""Append the value to an empty List"""

list = []
num = 0
print(num)
while num < 10:
    list.append(num)
    print("The value of num after append is " +str(num))
    num += 1
    print("The incremented value of num is " + str(num))
print(list)


