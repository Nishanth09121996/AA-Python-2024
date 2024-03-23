class Car:
    load_capacity = '400 Kg'
    def __init__(self, wheel_numbers:int, price:int, brand:str,make_year:int) -> None:
        self.wheel_numbers = wheel_numbers
        self.price = price
        self.brand = brand
        self.make_year = make_year
        self.vehicle_type = 'Car'
    
    def drive()->None:
        print('Driving ')
    
    def take_passenger() -> None:
        print('I can take passenger')

class Truck:
    load_capacity = '100 TON'
    def __init__(self, wheel_numbers:int, price:int, brand:str,make_year:int) -> None:
        self.wheel_numbers = wheel_numbers
        self.price = price
        self.brand = brand
        self.make_year = make_year
        self.vehicle_type = 'Truck'
        self.mutliaxle = True
    
    def drive()->None:
        print('Driving ')
    
    def take_passenger() -> None:
        print('I can take passenger')
        
car_obj = Car(wheel_numbers=4,price=40000,brand='Hyundai',make_year=2024)

truck_obj = Truck(wheel_numbers=14,price=40000000,brand='VolVo',make_year=2024)


print('The car name is {} and it has {} and price is {} make year of {} and Load Capacity of {} '.format(car_obj.brand,car_obj.wheel_numbers,car_obj.price,car_obj.make_year,car_obj.load_capacity))
print('The Truck name is {} and it has {} and price is {} make year of {} and Load Capacity of {} ans is mutile '.format(truck_obj.brand,truck_obj.wheel_numbers,truck_obj.price,truck_obj.make_year,truck_obj.load_capacity))
