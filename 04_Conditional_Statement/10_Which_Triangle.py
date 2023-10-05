"""
Write a program to input from user three numbers(A, B & C)
representing side lengths of a triangle.
You have to print if the triangle is "equilateral", "scalene" or "isosceles".
"""

try :
    A = int(input("Enter a side 1 : "))
    B = int(input("Enter a side 2 : "))
    C = int(input("Enter a side 3 : "))

    if A == B and B == C:
        print("equilateral")
    elif A == B or B == C or C == A:
        print("isosceles")
    else:
        print("scalene")
except:
    print("Enter a positive integer")
