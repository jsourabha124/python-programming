# Write a program to input an integer from user and print 1 if it is odd otherwise print 0.

try:
    num = int(input("Enter a integer number : "))
    if num % 2 == 0:
        print("1")
    else:
        print("0")
except:
    print("Please enter valid Integer number")
