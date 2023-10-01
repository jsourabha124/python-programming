# Vehicle management
"""
Imagine you want to create a program that manages different types of vehicles,
such as cars and bicycles. Each vehicle can perform actions like "start" and "stop,
" but the way they start and stop is different. Additionally, you want to be able to
calculate the fuel efficiency for cars and the pedal efficiency for bicycles.
"""

from abc import ABC, abstractmethod


class Vehical(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehical):
    def start(self):
        return f"{self.name} start by turning ignition key"

    def stop(self):
        return f"{self.name} stop by turning off ignition key"

    def calculate_fuel_eff(self, distance, fuel_consumed):
        return distance / fuel_consumed


class Bicycle(Vehical):
    def start(self):
        return f"{self.name} start from pedaling"

    def stop(self):
        return f"{self.name} stops by stopping peadling"

    def calculate_pedal_efficiency(self, distance, calories_burned):
        return distance / calories_burned


# create object
car = Car("Tata")
bicycle = Bicycle("Atlas")

print(car.start())  # Tata start by turning ignition key
print(bicycle.stop())  # Atlas stops by stopping peadling

print(car.calculate_fuel_eff(200, 10))  # 20.0
print(bicycle.calculate_pedal_efficiency(10, 500))  #0.02

