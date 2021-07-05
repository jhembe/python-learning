#for the for loops, the variable initialised in the loop structure is called loop variable

#for the syntax

for item in "Python":
    print(item)

#using list

for item2 in ["Baye","Manga","Lois","Furaha","Chuchu","Collins"]:
    print(item2)

#for huge list of numbers, we use a function "Range"

for item3 in range(50):
    print(item3) # --- This will print out all the numbers from 0 to 49

#also we can define te starting point and the ending point we pass argument in the range function
for item4 in range(5,16):
    print(item4)

# we can also use the step in the range function.
# The step argument describes how much number the iteration must must be skiped
for item5 in range(5,16,2):
    print(item5)

#### Now we are going to impose some string functionalities in the our loop print using a defined list
cars = ["Toyota","Audi","Suzuki","Honda","BMW","McLaren","Jeep","Mercedes"]

for car in cars:
    print(f'{car} - Thats bassically a great car')
    print(f'I cant wait for  to release another car version')
print("Well done to every car that has passed through. Thank you so much")

