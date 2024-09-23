# from Day4 import guess
# from Day4 import guess
# import random
#
# word_list = ["aardvark", "baboon", "camel"]
#
# # TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
#
# # TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#
# # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
# #  is, "Wrong" if it's not.
#
#
# chosen_word = random.choice(word_list)
# print(chosen_word)
#
# guess = input("Hi  guess the letter ").lower()
# print(guess)
#
#
# # while guess != chosen_word:
#
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")


import random
word_list = ["chandu", "theju", "ambi"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
# word_length = len(chosen_word)
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

display = ""

while display != chosen_word:
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
    print(display)
print("Wow You won")
