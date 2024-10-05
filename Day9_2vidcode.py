from Day9 import logo


print(logo)

bidders_list = {}


loop = True

def winner(final_list):
    highest = 0
    winner_name = ""
    for bidder_name in final_list:
        high = bidders_list[bidder_name]
        if high > highest:
            highest = high
            winner_name = bidder_name
    print(f"Thank You\nThe winner is {winner_name} & Highest bid amount is {highest}")


while loop:
    name = input("Please Enter Your Name :\n")
    bid = int(input("Please Enter The Bid Amount :\n"))
    next_bidders = input("Is There any Other User Who want to bid ? Type 'yes' or 'no'\n").lower()

    if next_bidders == "yes":
        print("\n" *10)
        bidders_list[name] = bid
        # print(bidders_list)
    elif next_bidders == "no":
        loop = False
        winner(bidders_list)






    else:
        print("Please Enter Vaild Input")