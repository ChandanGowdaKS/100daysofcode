# def chandan():
#     name = "Theju"
#     print("Hi Chandu")
#     return name
#
#
#
# output = chandan()
# print(output + "cha")

'''Let’s start simple: Write a Python function that prompts the user to enter a number. Then, given that number,
 it prints the sentence "Hello, Python!" that many times.'''
from Day4 import user_input


# from curses.ascii import isupper, islower

# def input_num(num):
#     print("Hello world\n" * (num))
#     return num
#
#
# user = int(input("enter the number: "))
# back = input_num(user)
# input_num(user)
# print(back)

# upper_case = 0
# lower_case = 0
# others = 0
# alpha_list = {}
#
# def letter_calculation(upper_case,lower_case,others):
#
#     string_input = input("Enter Anything")
#     for upcase in string_input:
#         if upcase.isupper():
#             upper_case += 1
#         elif upcase.islower():
#             lower_case += 1
#         else:
#             others += 1
#
#     alpha_list["upper"] = upper_case
#     alpha_list["lower"] = lower_case
#     alpha_list["others"] = others
#
#     return alpha_list
#     # print(alpha_list)
#
#
# back = letter_calculation(upper_case,lower_case,others)
# print(back)
nam = input("enter Your Name:\n")
def names(nam):
    print(f"Hi {nam}")
    user1 = int(input("Enter 1 For Addition\n2. for Sub\n3. For Mul \n4. For div  \n"))
    calculation(user1)


def calculation(user_inp):
    num1 = int(input("Enter The First Number: \n"))
    num2 = int(input("Enter The  Second Number :\n"))
    if user_inp == 1:
        print(num1+num2)
    elif user_inp == 2:
        print(num1-num2)
    elif user_inp == 3:
        print(num1*num2)
    elif user_inp == 4:
        print(num1/num2)
    else:
        print("Invalid Bro")


names(nam)



































