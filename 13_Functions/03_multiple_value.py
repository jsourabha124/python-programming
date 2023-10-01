# return multiple value : mini calculator

def mini_calculator(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    dev = x / y
    mod = x % y
    floor = x // y

    return add, sub, mul, dev, mod, floor


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
result = mini_calculator(num1, num2)

# unpack all return values into individual variables
addition, subtraction, multiplication, division, modulo, floor = result

print(f"addition : {addition}")
print(f"subtraction : {subtraction}")
print(f"multplication : {multiplication}")
print(f"division : {division}")
print(f"modulo : {modulo}")
print(f"floor : {floor}")

