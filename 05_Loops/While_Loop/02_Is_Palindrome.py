"""
Check Palindrome for numbers.
take integer N as input and Check whether that number is Palindromic / Not Palindromic.
Input :
101
51

Output 1:
Palindromic
Not Palindromic
"""


def reverse_number(num):
    rev = 0
    while num > 0:
        mod = num % 10
        rev = (rev * 10) + mod
        num = num // 10
    return rev


N = int(input("Enter a Number : "))
res = reverse_number(N)

if N == res:
    print("Palindromic")
else:
    print("Not Palindromic")
