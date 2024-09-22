# from Day4 import user_input
# from Day4 import user_input

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

chosen_word = "camel"

user_inputt = input("enter the guessed letter to check")

while user_inputt != chosen_word:
    user_inputt = input("enter the guessed letter to check")
    for letter in chosen_word:
        if letter == user_inputt:
            print("Right")
        else:
            print("Wrong")
