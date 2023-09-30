# There are 4 types of string interpolations are exist in python, namely
"""
1. Modulo(%) interpolation
2. .format interpolation
3. f-format interpolation
4. concatination
"""
name = "Joshi"
age = "27"
# modulo interpolation
# module_message = "Am %s and my age is %d" %(name, age)

# format interpolation
format_message = "I am {} and my age is {}".format(name, age)
print(format_message)  # I am Joshi and my age is 27

# f-formate interpolation
f_formate_message = f"I am {name} and my age is {age}"
print(f_formate_message)  # I am Joshi and my age is 27

# concatination interpolation
concatination_string = "I am " + name + " and my age is " + str(age)
print(concatination_string)  # I am Joshi and my age is 27
