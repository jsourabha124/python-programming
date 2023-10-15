"""
Given a number N, print reversed of N.
Input 1 :
12054

Output 1 :
45021
"""

N = int(input("Enter a number : "))
num = N
rev = 0
while N > 0:
    mod = N % 10
    rev = (rev * 10) + mod
    N = N // 10

print(f"Given Num : {num} and Reverse Num is : {rev}")
