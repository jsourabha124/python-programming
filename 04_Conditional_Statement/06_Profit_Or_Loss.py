"""
You are given the Cost Price C and Selling Price S of a Product.
You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss.

NOTE: It is guaranteed that Cost Price and Selling Price are not equal.
"""

try:
    cost_price = float(input("Enter a cost price : "))
    sell_price = float(input("Enter a sell price : "))

    if cost_price == sell_price:
        print("Cost price and sell price should not be equal")
    else:
        if cost_price < sell_price:
            print("Profit")
        else:
            print("Loss")
except:
    print("There is some error")
