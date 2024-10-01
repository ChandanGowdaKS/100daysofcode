# def greet():
#     print("Hello World")
#     print("Hello Chandu")
#     print("Hello Theju")
#
# greet()

# def greet_with(name,location):
#     print(f"Hi {name}")
#     print(f"what is the Special in your location {location}")
# greet_with("chandu","channapatna")

'''Love Calculator
💪 This is a difficult challenge! 💪

You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people:

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.

2. Then check for the number of times the letters in the word LOVE occurs.

3. Then combine these numbers to make a 2 digit number and print it out.

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53 '''


def calculate_love_score(name1, name2):
    count = 0
    count2 = 0
    li = ['t', 'r', 'u', 'e']
    li2 = ['l', 'o', 'v', 'e']
    for name in name1:
        for name3 in li:
            if name3 == name:
                count += 1
    for name4 in name2:
        for name5 in li:
            if name5 == name4:
                count += 1
    print(f"TRUE Total = {count}")

    for name in name1:
        for name3 in li2:
            if name3 == name:
                count2 += 1
    for name4 in name2:
        for name5 in li2:
            if name5 == name4:
                count2 += 1
    print(f"Love Total = {count2}")
    print(f"Total Love Score = {count}{count2}")


calculate_love_score("chandu", "prameela")


# Sep 29/9/24

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# 30/9 sep Not Tried

letter2 = []
decode = ''
def encrypt(original_text,shift_amount):
    for alpha in original_text:
        encode = alphabet.index(alpha)
        letter2 = letter.append(encode)
        print()
        
        for decode2 in encode:
            decode = decode2.[]

encrypt("chandu",2)




