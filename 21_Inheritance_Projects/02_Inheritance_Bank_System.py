# Banking system

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("User Information ")
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Gender : ", self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposite(self, amount):
        self.amount = amount
        self.balance += self.amount
        print("Account balance updated : ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if (amount > self.balance):
            print("Insufficient balance | avilable balance is ", self.balance)
        else:
            self.balance -= self.amount
            print("Account balance updated : ", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance is ", self.balance)


user1 = Bank("Sourabha", 25, 'M')
user2 = Bank("Sachin", 24, 'M')
user3 = Bank("Sudhamani", 50, 'F')

#operations
print(user1.deposite(100))
print(user2.deposite(255))
print(user3.deposite(500))

print(user1.view_balance())
print(user2.view_balance())
print(user3.view_balance())

print(user1.withdraw(500))
print(user2.withdraw(200))
print(user3.withdraw(300))