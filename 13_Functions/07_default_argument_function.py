# default argument : Default argument will consider if the argumnet is not provided in function call

def default_argument(full_name, age="25"):
    print(f"I am {full_name} and my age is {age}")


name = input("Enter a name : ")
# function call
default_argument(name)
