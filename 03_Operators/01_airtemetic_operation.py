def addition_num(x, y):
    return x + y


def subtraction_num(x, y):
    return x - y


def multiplication_num(x, y):
    return x * y


def division_num(x, y):
    return x / y


def devision_floor_num(x, y):
    return x // y


def power_num(x, y):
    return x ** y


def modulo_num(x, y):
    return x % y


num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))

add = addition_num(num1, num2)
sub = subtraction_num(num1, num2)
mul = multiplication_num(num1, num2)
dev = division_num(num1, num2)
dev2 = devision_floor_num(num1, num2)
powr = power_num(num1, num2)
mod = modulo_num(num1, num2)

print(f"Addition : {add}, subtraction : {sub}, Multiplication : {mul}, Division : {dev}, Division2 : {dev2}, Power_Of : {powr} and Modulo : {mod}")
