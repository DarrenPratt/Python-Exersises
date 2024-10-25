my_money = 9

if my_money > 10:

    print("You have sufficient funds in your account.")

else:

    print("There is not enough money in your account to complete the purchase.")

#You can also chain comparators in a conditional. In the example below, 
# the conditional checks two comparators: whether a deposit is greater than 0 but not above a maximum deposit amount:

deposit = 15

if 0 < deposit <= 100:

    print(f"Thank you for the £{deposit} deposit!")

else:

    print("This is not a valid amount to deposit.")