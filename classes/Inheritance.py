# Inheritance is basically  a mechanism of re-using code..




class Mammal:
    def __init__(self,name,leg_count,color):
        self.name = name
        self.leg_count = leg_count
        self.color = color

    def walk(self):
        print(f"{self.name} can walk")
    
# NOTE in order to show / innitialise inheritance then we add parenthesis after the class name     
class Dog(Mammal):
    def dog_name(self):
        print(f"My dog name is {self.name}, he has {self.color} color")

class Cat(Mammal):
    pass


dog1 = Dog("Pookie",4,"White")
print(dog1.dog_name())


cat1 = Cat("Cookie",4,"Brown")
print(cat1.color)
print(cat1.walk())