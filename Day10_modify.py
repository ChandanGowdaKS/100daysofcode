



''' Caluculator Using Function '''

''' My Code Only , But Some Modification in Functions After Seeing video '''





def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2


operation_dict = {"+": add, "-": sub, "*":mul, "/":div}





def arithematic_operation():
    looping = True
    first_number = float(input("Please Enter The first Number :\n"))
    while looping:
        # previous = result

        choose = input('''Select the operation :\n
"+"\n"-"\n"*"\n"/"\n''')

        second_number = float(input("Enter The Next Number :\n"))

        result = operation_dict[choose](first_number,second_number)

        result_output = (f"{first_number}{choose}{second_number} = {result}")
        print(result_output)

        loop = input('''Do You Want To Continue Operations With Old Result,
If yes Type 'y' , If To restart From Starting Type 'n' , Type 's' To stop & see final Result \n''').lower()

        if loop == "y":
            looping = True
            first_number = result
        elif loop == 'n':
            looping = False
            print("\n"*20)
            arithematic_operation()
        elif loop == 's':
            looping = False
            print(f"The Final Result is {result_output}")

        else:
                print("Invalid Input")


arithematic_operation()