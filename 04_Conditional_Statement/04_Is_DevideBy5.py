"""
Given a Number N. If number is divisible by 5,
print "Divisible by 5".
Otherwise print "Not divisible by 5".
"""

try:
    num = int(input("Enter a integer value : "))

    if num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")
except:
    print("Enter a valid integer")
