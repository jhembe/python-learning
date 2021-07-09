import random
# NOTE, this is the built in module normally used to generate random values
# we can also use the "." operator to get to know about the functions it has

for i in range(3):
    print(random.random())

#if we want to pass random integer values within a certain range we use randint() or randrange()

for i in range(5):
    print(random.randint(10,40))
print("\n")

for i in range(5):
    print(random.randrange(10,40))