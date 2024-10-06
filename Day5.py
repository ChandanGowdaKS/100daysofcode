# # Adding All 1-100 numbers

sum = 0

for num in range(1,101):
    sum += num
print(sum)

 ''' FizzBuzz Game
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
Your program should print each number from 1 to 100 in turn and include number 100.
But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz" '''

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)

#  Password Generator

import random

print("Hi welcome To Password Generator")

password = ""

Big_letter = ["A","B","C","D","E","F","G","H","I",'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Small_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1','2','3','4','5','6','7','8','9']
special_letter = ['!','@','#','$','%']

big_char_input = int(input("How many Big Letters Do you want In Your Password ?"))
small_char_input = int(input("How many Small Letters Do you want In Your Password ?"))
number_input = int(input("How many numbers Do you want In Your Password ?"))
special_char_input = int(input("How many Special Letters Do you want In Your Password ?"))

for num in range(0,big_char_input):
    password += random.choice(Big_letter)
for num in range(0,small_char_input):
    password += random.choice(Small_letter)
for num in range(0,number_input):
    password += random.choice(number)
for num in range(0,special_char_input):
    password += random.choice(special_letter)

print(password)
password = list(password)
random.shuffle(password)

password2 = ""
for passw in password:
    password2 += passw

print(f"Your password Created Successfully, You Password is {password2})


