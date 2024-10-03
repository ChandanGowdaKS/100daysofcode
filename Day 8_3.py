# from curses.ascii import isalpha
#
# from unicodedata import numeric
from math import trunc

from select import select

from Day8_2 import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']






# TODO-2: What happens if the user enters a number/symbol/space?

# Type 'yes' if you want to go again. Otherwise, type 'no'.
#
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again
rerun = True

while rerun == True:
    encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))



    def caesar(original_text,shift_amount,selection):
        if encode_decode == "decode":
            shift_amount *= -1
        word = ""

        for letter in original_text:
            if letter.isalpha():
                shifted_letter = alphabet.index(letter) + shift_amount
                shifted_letter %= len(alphabet)
                word += alphabet[shifted_letter]
            else:
                word += letter

        print(word)


    caesar(text,shift,encode_decode)

    opt = input("Do You Want To Rerun The Program Type 'yes' Otherwise 'No' !!").lower()
    if opt == "no":
        print("Thank you Bye")
        rerun = False

