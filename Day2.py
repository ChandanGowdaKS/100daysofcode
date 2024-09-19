# In Day 2, I learnt data types,data type casting,f strig.

# Today am going to try Bill dividing Calculator.

bill = int(input("Thanks for visiting our Hotel, Please enter Your Bill to Calculate Dividing Amount!!\n "))
tips = int(input("Please add Tips in percentage ex: 10,20,30\n"))
members = int(input("Thanks For Adding a Tip, Please Enter How many members To Split the Bill\n"))
final_amount = tips/100 *bill +bill
divided_amount = final_amount/members
print(f"Final Amount to be Paid is {final_amount}/- only")
print(f"Every member has to pay is {divided_amount}/- only ")
