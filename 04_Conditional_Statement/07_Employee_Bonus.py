"""
A company decided to give bonus of 5% to employee if his/her year of service
is more than 5 years. Ask user for their name and year of service and print
whether they should recieve bonus or not.

Note : 1 <= years of service <= 100
"""

try:
    employee_name = input("Enter a name : ")
    employee_service = int(input("Enter a service : "))

    if (employee_service >= 1 and employee_service <= 100):
        if employee_service >= 5:
            print(f"{employee_name} will receive Bonus")
        else:
            print(f"{employee_name} will not receive Bonus")
    else:
        print("Please enter service between 1 to 100 years")
except:
    print("Some error occur")
