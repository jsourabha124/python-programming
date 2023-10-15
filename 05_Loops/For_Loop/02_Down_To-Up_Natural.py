"""
Write a program that takes a positive integer N as input from the user and prints all natural numbers from 1 to N,
with each number followed by a space (including the last number).
N = 5
o/p : 5 4 3 2 1
"""

N = int(input("Enter a number : "))

for i in range(N, 0, -1):
    print(i, end=" ")