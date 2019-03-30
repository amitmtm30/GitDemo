def ExceptionHandlingExercise():

    # try:
    #     car = {"Make" : "BMW", "Model" : "530i", "Year" : "2018"}
    #     print(car['Color'])
    #
    # except:
    #     print ("Color Key is not found")
    #
    # finally:
    #     print("This is executed")
# ExceptionHandlingExercise()

#     """Exception Division by 0 Example 1 """
#
#     a = 10
#     b = 20
#     c = 0
#     d = (a+b) / c
#     print(d)
# # ExceptionHandlingExercise()
#
#     """Exception Type error Example 2 """
#
#     a = 10
#     b = 'Any Integer'
#     c = 0
#     d = (a + b) / c
#     print(d)
# ExceptionHandlingExercise()

#     """Exception Handle Example 1 """
#     try:
#         a = 10
#         b = 20
#         c = 0
#         d = (a+b) / c
#         print(d)
#     except:
#         print('I am in Except block')
# ExceptionHandlingExercise()


#     """Exception Handle Example 2 """
#     try:
#         a = 10
#         b = 20
#         c = 0
#         d = (a+b) / c
#         print(d)
#     except ZeroDivisionError:
#         print('I am in Except block')
# ExceptionHandlingExercise()

#     """Exception Handle Example 3 """
#     try:
#         a = 10
#         b = 'Any Integer'
#         c = 30
#         d = (a + b) / c
#         print(d)
#     except TypeError:
#         print('I am in Except block')
#
#
# # ExceptionHandlingExercise()
# #
# #     """Exception Handle Example 4 """
# #     try:
# #         a = 10
# #         b = 20
# #         c = 0
# #         d = (a + b) / c
# #         print(d)
# #     except:
# #         print('I am in Except block')
# #     else:
# #         print("No Exception Found")
# #
# #     finally:
# #         print("I am always Executed ")
# #
# # ExceptionHandlingExercise()

    # ExceptionHandlingExercise()

    """Exception Handle Example 5 """
    try:
        a = 10
        b = 20
        c = 0
        d = (a + b) / c
        print(d)
    except:
        print('I am in Except block')
        raise Exception('This is  an exception')
    else:
        print("No Exception Found")

    finally:
        print("I am always Executed ")


ExceptionHandlingExercise()
