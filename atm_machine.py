#atm machine
amount = 100000


option1 = "1.Check balance"
option2 = "2.Deposit money"
option3 = "3.Withdraw money"

print("Hello! Welcome to sample ATM machine")
print("Please insert your card")
print("Choose one option below to proceed")
print("NOTE::: Please enter selected option with number as same as you look")
print("-----------------------------------")
print(option1 , option2, option3 , sep = ',')
print("-----------------------------------")

choose = input("Enter your selected option to continue! ")

if choose == option1:
    print(f"Your total available balance is: {amount}")
elif choose == option2:
    deposit = int(input("Enter your deposit amount: "))
    total_amount = deposit + amount
    print(f"Your total balance is: {total_amount}")
elif choose == option3:
    withdraw = int(input("Enter the amount you want to withdraw: "))
    print("Take your cash")
    available_balance = amount - withdraw
    print(f"Your total available balance after withdraw is: {available_balance:}")
    
else:
    print("Invalid Option")
    
    
print("Please take your card")
print("Visit again")
    


# if choose == option1:
#     print(input(f"Your balance is:{amount} "))
# elif choose == option2:
#     deposit_amount = int(input("How much you want to deposit? "))
#     amount = amount + deposit_amount  # Update the actual balance
#     print("Your amount has been successfully deposited to your account :) ")
#     print(f"Your total available amount is: {amount}")
# elif choose == option3:
#     withdraw_amount = int(input("How much you want to withdraw? "))
#     if withdraw_amount <= amount:
#         amount = amount - withdraw_amount  # Update the actual balance
#         print("Please collect your cash.")
#         print(f"Your remaining balance is: {amount}")
#     else:
#         print("Insufficient balance!")
# else:
#     print("Invalid option..Try again")
