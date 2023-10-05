"""
Check whether a given number is positive-odd, positive-even, negative-odd OR negative-even.
Write a code to figure out the Situation.
Take a number N from user and print the Situation Of Number.
if positive-odd : print -> "Number is Positive and Odd"
if positive-even : print -> "Number is Positive and Even"
if negative-odd : print -> "Number is Negative and Odd"
if negative-even : print -> "Number is Negative and Even"
"""

try:
    num = int(input("Enter a number : "))

    if num > 0:
        if num % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")
    else:
        if num % 2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")
except:
    print("Please enter a integer number ")
