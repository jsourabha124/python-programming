"""
You are given 3 integer angles(in degrees) A, B and C of a triangle.
You have to tell whether the triangle is valid or not.
A triangle is valid if sum of its angles equals to 180.

Print 1 if the triangle having given sides is valid, else print 0.
"""

try:
    A = int(input("Enter side 1 : "))
    B = int(input("Enter side 2 : "))
    C = int(input("Enter side 3 : "))

    if A == B == C:
        print("1")
    else:
        print("0")

except:
    print("Enter integer values")
