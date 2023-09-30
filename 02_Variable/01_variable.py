# variables : Which store memory location to store the value

# Simple Variable Assignment and Printing
str_name = "Joshi Sourabha"
print(str_name)

# Numeric Operations with Variables
x = 10
y = 20

sum_value = x + y
product_value = x * y

# print("Sum of " + x + " and" + y + " is " + sum_value) #only we can concatinate string not int : Error

# convert int value to string
print("Sum of " + str(x) + " and" + str(y) + " is " + str(sum_value))  # Sum of 10 and20 is 30

# By using f-formate also we can display
print(f"Product of {x} and {y} is {product_value}")  # Product of 10 and 20 is 200
