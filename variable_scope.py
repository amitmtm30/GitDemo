
"""Local Variable"""
# a = 11
# #
# # def test_method(a):
# #     print("Value of local 'a' is" +str(a))
# #
# #     a = 2
# #     print("Value of local 'a' is" + str(a))
# #
# # print("Value of global 'a' is " +str(a))
# #
# # test_method(a)
# #
# # print("Did the value of global changed" +str(a))

"""Global Variable"""

a = 11

def test_method():
    global a
    print("Value of local 'a' inside the method is" +str(a))

    a = 2
    print("Value of local 'a' inside the method is" + str(a))

print("Value of global 'a' is " +str(a))

test_method()

print("Did the value of global value 'a' is changed " +str(a))