"""
Indentation refers to the spaces at the beginning of a code line. It is very important as Python uses
indentation to indicate a block of code.If the indentation is not correct we will endup with
IndentationError error.
"""

# Ex : return true
num = 10
if num == 10:
    print("True")

# Ex : Through error
num2 = 20
# if num2 == 20:
# print("True")  # IndentationError: expected an indented block after 'if' statement on line 14

# Ex : for loop
for i in range(0, 5):
    print(i)
