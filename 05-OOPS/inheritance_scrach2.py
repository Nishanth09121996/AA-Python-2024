# Parent Class
class Vehicle:
    def __init__(self,license_no:str,wheels:int, brand:str,load_capacity:str,price:int,make:int) -> None:
        self.license_no = license_no
        self.wheels = wheels
        self.brand = brand
        self.load_capacity = load_capacity
        self.price = price
        self.make = make
        self.color = 'Red'

    def drive(self)->None:
        print('This vechicle can drive')
    
    def take_load(self)->None:
        print('I Can Take the load')

    def print_details(self)->None:
        print('The vec make year is  {} as {} wheels and  brand is {}'.format(self.make,self.wheels,self.brand))
# Child Class 1

class Car(Vehicle):
    has_cooler = True
    type = 'Car'
    def __init__(self, license_no: str, wheels: int, brand: str, load_capacity: str, price: int, make: int) -> None:
        super().__init__(license_no, wheels, brand, load_capacity, price, make)
        

    def self_drive_passenger(self):
        print('The car can self Drive')

class Truck(Vehicle):
    has_mutiaxle = True
    Type = 'Truck'
    def __init__(self, license_no: str, wheels: int, brand: str, load_capacity: str, price: int, make: int) -> None:
        super().__init__(license_no, wheels, brand, load_capacity, price, make)    
    
    def has_more_than_8_wheels(self):
        print('All Truck are multiple has multiple wheels')
    
    def check_multi_axle():
        pass

car  = Car(license_no='TN12 ABCD',wheels=4,brand='TATA',load_capacity='5 Passengger',price=400000,make=2024)
truck = Truck(license_no='111',wheels=16,brand='Scanaia',load_capacity='100 tons',price=5000000,make=2023)
car.print_details()
car.self_drive_passenger()
car.take_load()
print('-------------------------------')
truck.print_details()
truck.drive()
truck.has_more_than_8_wheels()