"""
You take a number of test cases, denoted by T as input.
For each test case, you should take integers N as input.
Your task is to calculate and print the sum of the digits of the given number N.

Input 1:
2
5
1001

Output 1:
5
2
"""

T = int(input("Enter number of iteration : "))

for i in range(1, T+1):
    sum = 0
    N = int(input("Enter number : "))

    while N > 0:
        mod = N%10
        sum += mod
        N = N//10
    print(f"Sum : {sum}")