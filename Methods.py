"""To Define Methods"""

# def num_sum():
#     print(3 + 2)
# num_sum()
#
# """With Argument"""
# def sum_num(n1 , n2):
#     print (n1 + n2)
#
# sum_num(3,4)
#
# """Return Value"""

# def sum_num(n1,n2):
#     """Get some of two numbers
#     :param n1:
#     :param n2:
#     :return :
#     """
#     return n1 + n2
# sum1 = sum_num(4,5)
# print(sum1)

""" With the Positional Parameter"""

def sum_num (n1 = 4 , n2 = 10):
    return n1 + n2
sum1 = sum_num(10)
sum1 = sum_num(20,10)
sum1 = sum_num(n2=20)
sum1 = sum_num(n1=20)
print(sum1)

