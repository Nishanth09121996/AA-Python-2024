from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,num_of_legs:int,food_type:str,number_eys:int,animal_name:str) -> None:
        self.num_of_legs = num_of_legs
        self.food_type = food_type
        self.number_eys = number_eys
        self.animal_name = animal_name
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    animal_class = 'Lion'
    def __init__(self, num_of_legs: int, food_type: str, number_eys: int, animal_name: str, i_am_hunter:bool, character:list) -> None:
        super().__init__(num_of_legs, food_type, number_eys, animal_name)
        self.characters = character
        self.is_hunter = i_am_hunter
    def eat(self):
        print('Animal should eat something')
    def sleep(self):
        print('Animal should Sleep')

lion_obj = Lion(num_of_legs=4,food_type='Carnivorous',number_eys=2,animal_name='Symba',i_am_hunter=True,character=['eat','sleep','hunt','run','jump'])

print('_____________')
print("{} belong to  class {} , it has {} legs , {} eyes and it is {} species which can hunt on animals "\
      .format(lion_obj.animal_name,lion_obj.animal_class,lion_obj.num_of_legs,\
              lion_obj.number_eys,lion_obj.food_type))

