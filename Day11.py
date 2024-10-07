# Black Jack Game

import random
from distutils.command.build_scripts import first_line_re
from importlib import invalidate_caches


def logo():
    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")

logo()

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

computer_list = []
player_list =[]

name = input("Enter Your Name :\n").title()




def continue_game():

    comp_score = 0
    player_score = 0
    first = True
    while first:
        game = input(f'''Hi {name} Do You want to play Blackjack Game,
if Yes Type "y", If No Type "n"\n''').lower()
        if game == "y":
            for i in range(2):
                computer = random.choice(cards)
                computer_list.append(computer)
                comp_score += computer
                player = random.choice(cards)
                player_list.append(player)
                player_score += player

            print("Computer's First Card is :",computer_list[0])
            print(f"{player_list} {name} Your Score is {player_score}\n")

            second = True
            while second:
                next_card = input(f"{name} Do you Want One More Card Type 'y' or 'n' \n")
                if next_card == "y":
                    player = random.choice(cards)
                    player_list.append(player)
                    player_score += player
                    print("Computer's First Card is :",computer_list[0])
                    print(f"{player_list} {name} Your Score is {player_score}\n")
                elif next_card == "n":
                    second = False
                    print(f"Computer's Score is {comp_score}" )
                    print(f"{player_list} {name} Your Score is {player_score}\n")
                    if player_score <= 21:
                        if comp_score <= 21:
                            if player_score > comp_score:
                                print(f"{name} You won, Your Score is {player_score}")
                            else:
                                print(f"{name} You loose, Your Score is {player_score}")
                        else:
                            print(f"Computer Loose, Computer's Score is {comp_score}")

                    else:
                        print(f"{name} You Loose, Your Score is {player_score}")



                else:
                    print("Invalid input")

        elif game == "n":
            print(f"Thank you {name} See You Soon ")
            first = False
        else:
            print("Invalid Input")


continue_game()
