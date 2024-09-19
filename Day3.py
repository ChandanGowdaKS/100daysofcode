#                               Roller Coaster Ticket

print("Hi Welcome to Roller Coaster")

age = int(input("Please Enter Your Age"))
bill = 0

if age <= 12:
    print("Your Ticket Price is $7")
    bill = 7
elif age <=18:
    print("Your Ticket Price is $10")
    bill = 10
else:
    print("Your Ticket Price is $15")
    bill = 15

photo = input("Do You Want Photo, Which Will Cost extra $3, \n Type 'y' or 'n' ")
if photo == "y":
    print(f"Your Ticket Price is ${bill+3}")
else:
    print(f"Your Ticket Price is ${bill}")



#                         TREASURE GAME

print("Hi Welcome To Treasure Hunting")
print("Your Mission is To Find Treasure")
way = input("Type 'left' or 'right' to hunt the Treasure")
if way == "right":
    print("Sorry Game Over you Lose")
elif way == "left":
    print("Super!!")
    way2 = input( "Now Type 'swim' or 'wait' to Continue")
    if way2 == "swim":
        print("Sorry Game Over you Lose")
    elif way2 == "wait":
        print("Great Just One Step Away To the Treasure")
        way3 = input("Now Which Door are You going To Choose, 'red','yello','blue'.")
        if way3 == "red" or way3 == "blue":
            print("Sorry Game Over you Lose")
        elif way3 == "yellow":
            print("Wow You Won")
        else:
            print("Please Enter Valid Input")
    else:
        print("Please Enter Valid Input")
else:
    print("Please Enter Valid Input")

