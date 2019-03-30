"""Tupples are very much similar to List but only change is that the tupples are immutable
It mean's you can not change it
In Tupples only two methods available 1. find index : Find the indexes of the element
2.  Count : It finds out the number of times the particular item appears
"""
my_tupple = (1,2,2,2,3,3,3,4,4,4,4,3)
print(my_tupple)
# my_tupple[0] = 0
print(my_tupple[0])
print(my_tupple[1:])
print(my_tupple.index(2))
print(my_tupple.count(2))