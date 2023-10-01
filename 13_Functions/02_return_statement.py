# Return statement : return addition of numbers

def add_values(x, y):  # function definition
    return x + y  # return statement terminates the function block


num1 = int(input("Enter a num1 : "))
num2 = int(input("Enter a num2 : "))
result = add_values(num1, num2)  # function call
print(result)
