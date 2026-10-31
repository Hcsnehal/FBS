from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def calculate_toll(self, persons):
        pass

class TwoWheeler(Vehicle):
    def calculate_toll(self, persons):
        amount = 20
        if persons > 2:
            amount += (persons - 2) * 10
        return amount
class ThreeWheeler(Vehicle):
    def calculate_toll(self, persons):
        amount = 30
        if persons > 3:
            amount += (persons - 3) * 20
        return amount

class FourWheeler(Vehicle):
    def calculate_toll(self, persons):
        amount = 40
        if persons > 4:
            amount += (persons - 4) * 40
        return amount

class HeavyVehicle(Vehicle):
    def calculate_toll(self, persons):
        amount = 60
        if persons > 6:
            amount += (persons - 6) * 100
        return amount
while True:
    print("\n----- TOLL PLAZA -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Thank you!")
        break

    persons = int(input("Enter number of persons: "))
    if choice == 1:
        obj = TwoWheeler()

    elif choice == 2:
        obj = ThreeWheeler()

    elif choice == 3:
        obj = FourWheeler()

    elif choice == 4:
        obj = HeavyVehicle()
    else:
        print("Invalid choice!")
        continue
    total = obj.calculate_toll(persons)
    print("Total Toll Amount = Rs.", total)