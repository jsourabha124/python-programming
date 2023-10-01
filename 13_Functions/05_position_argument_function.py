# Position argument : position of argument during function call should match with function defination

def position_argument(first_name, last_name, age):
    print(f"First name : {first_name}, Last name : {last_name} and Age is : {age}")


f_name = input("Enter first name : ")
l_name = input("Enter last name : ")
age = int(input("Enter age : "))

# function call
position_argument(f_name, l_name, age)
