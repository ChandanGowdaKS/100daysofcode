
''' Caluculator Using Function'''
'''My Own Code Using Only Question'''



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







