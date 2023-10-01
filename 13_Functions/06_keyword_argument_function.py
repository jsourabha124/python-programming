# Keyworkd argument : Allow to provide keyword while calling function call
# keyword allow to pass argument out of order

def keyword_args(fullname, years):
    print(f"I am {fullname} and my age is {years}")


name = input("Enter a name : ")
age = int(input("Enter a age : "))

# function call
keyword_args(years=age, fullname=name)
