"""
Write a program to input three numbers(A, B & C) from user and
print the maximum element among A, B & C in each line.
"""

try:
    A = int(input("Enter number 1 : "))
    B = int(input("Enter number 2 : "))
    C = int(input("Enter number 3 : "))

    if A > B and B > C:
        print("A is greater")
    elif B > C:
        print("B is greater")
    else:
        print("C is greater")
except:
    print("Enter positive integer numbers")