# def name(f_name,l_name):
#     fname = f_name.title()
#     lname = l_name.title()
#     print(fname,lname)
#     return fname,lname
#
# name("chandu","gowda")
'''
def is_leap_year(year):
    operation = []
    operation.append(year / 4)
    operation.append(year / 100)
    operation.append(year / 400)
    for op in operation:
        if op == float(op):
            print("Its not a Leap year")
            # return True
    print("Its a Leap year")
    # return False

is_leap_year(2024)'''
from email.contentmanager import set_text_content

# def my_function(a):
#     if a > 40:
#         return
#         print("Terrible")
#     if a > 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))

''' Caluculator Using Function'''

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


operation_dict = {"+": add, "-": sub, "*":mul, "/":div}


first_number = float(input("Please Enter The first Number :\n"))

choose = input('''Select the operation :\n
"+"\n"-"\n"*"\n"/"\n''')

second_number = float(input("Enter The Second Number :\n"))

result = operation_dict[choose](first_number, second_number)
result_output = (f"{first_number}{choose}{second_number} = {result}")
print(result_output)

looping = True
loop = input('''Do You Want To Continue Operations With Old Result,
If yes Type 'y' , If No Type 'n'\n''').lower()
if loop == 'y':
    looping = True
elif loop == 'n':
    looping = False
    print(f"Final Result is {result_output}")
else:
    print("Invalid Input")

while looping:
    previous = result
    choose = input('''Select the operation :\n
"+"\n"-"\n"*"\n"/"\n''')

    second_number = float(input("Enter The Second Number :\n"))

    result = operation_dict[choose](previous,second_number)

    result_output = (f"{previous}{choose}{second_number} = {result}")
    print(result_output)

    loop = input('''Do You Want To Continue Operations With Old Result,
If yes Type 'y' , If No Type 'n'\n''').lower()

    if loop == "y":
        looping = True
    elif loop == 'n':
        looping = False
        print(f"Final Result is {result_output}")
    else:
            print("Invalid Input")







