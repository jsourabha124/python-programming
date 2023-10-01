# multiple return values

def is_logic_true(x, y):
    is_greater = x > y
    is_lesser = x < y
    is_equal = x == y

    return is_greater, is_lesser, is_equal


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

# function call
result = is_logic_true(num1, num2)

# unpack value to individual variable
greater, lesser, equal = result

print(f"is_greater : {greater}, is_lessaer : {lesser} and is_equal : {equal}")
