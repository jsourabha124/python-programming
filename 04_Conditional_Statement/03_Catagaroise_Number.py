"""
Write a program to input a number(A) from user and print 1 if it is positive,
-1 if it is negative, 0 if it's neither positive nor negative.
"""

try:
    num = int(input("Enter a number : "))

    if num > 0:
        print(1)
    elif num < 0:
        print(-1)
    else:
        print(0)
except:
    print("Enter  valid integer value")
