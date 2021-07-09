class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi {self.name} can talk')

person1 = Person("Joseph")
print(person1.name)
person1.talk()

person2 = Person("Bob")
print(person2.name)
person2.talk()

# Hence each object is a different instance of a person class


