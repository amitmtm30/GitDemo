"""Execute statements repeatedly
conditions are used to stop the execution of loops
Iterable items are String, List, Tuple, Dictionary
"""
""" For Loop as a string """
# my_string = 'abcabc'
# for amit in my_string:
#     # print(amit,end=" ")
#     if amit == 'a':
#         print("A", end= ' ')
#     else:
#         print(amit, end=' ')
#
# """For Loop as a List """
#
# cars = ['BMW','BENZ','HONDA']
# print(cars)
# print('*' *20)
#
#
# """Print as a List"""
#
# for car in cars:
#     print(car)
#     if car == 'BMW':
#         print('This is avery Gud car')
#     else:
#         print("No cars Available")
# num = [1,2,3]
# for n in num:
#     print(n * 10)
#
# """For Loop as a Dictionary """
#
# d = {'one' : 1, 'two' : 2, 'three' : 3}
# # for k in d:
# #     # print(k)
# #     print(k +" "+ str(k))
# for k,v in d.items():
#     print(k)
#     print(v)

"""############################# Print the number from 1 to 10 """
number = 10
for n in range(0, number,3):
    print(n)



