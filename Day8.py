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