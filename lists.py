#  # in order to write a list, you need to use the following syntax
#  # name_of_list = [content1,content2]
# #          0      1       2          3
# names = ["John","Bob","Gabriel","Gonzales"]
# print(names);

# # we can specify the index of the specific item in the list
# print(names[2]) 
# print(names[3])
# #we can also use the negative index to define elements in a list
# print(names[-2])
# print(names[-1])
# #we can also print the list of contents of in through the list

# print(names[2:])
# print(names[2:3])
# #we can also put only [:]
# print(names[:])

# names[0] = "Joseph"
# print(names)


#considet the following list

cars = ["Toyota","Audi","Suzuki","Honda","BMW","McLaren","Jeep","Mercedes"]
#Here below are the different functionalities that can be perfomed in a list

#printing list length
print(len(cars))
print(cars[2].title()) # the title finction changes the first letter of the string to be capitalised

#modifying elements in a list
#example, changing the second element of the sting to a number
# cars[2] = 5
# print(cars)

cars[2] = "tata"
print(cars)

#adding elements infront of the list.. Append

cars.append("Nissan")
print(cars)

cars.append("Ford Motors")
cars.append("Volkswagen")

print(cars)

#In order to insert elements in a list, then we use the insert function as below
cars.insert(0,"Porsche") # this will insert the element Porsche in the zero index
print(cars) 


##Now we can also remove elements in python list
# we can use the keyword del
# follow below
del cars[0]
print(cars)

# incase you want to use the value from the list after being deleted, we use the function with the 
#keyword pop
#by default the pop fuction removes the last ellement of the list, unless specified otherwise by
#passing the index of the desired popped value as an argument in the pop fuction

popped_car = cars.pop(2)
print(popped_car)
print(cars)
# using the popped value in a string sequence
print(f'The least car i like is the {popped_car.title()}.')
#mind you, that title is a function/method

##  we can also remove items in a list by values
removed_by_value = cars.remove("Nissan")
print(cars)
# You can also assign a variable then use it in the remove function without the need of putting quotations



#### Organising Lists

#consider the following list of fruits , that we are goig to  organise it using different ways
fruits = ["lemons","strawberries","oranges","lime","grape fruit","apples","pomegranate"]

# we can use the fuction sort() if we want to sort the list permanently
# fruits_sorted=fruits.sort()
# print(fruits_sorted)


# cars1 = ["bmw","audi","toyota","subaru"]
# cars1.sort()
# print(cars1)
fruits.sort()
print(fruits)
#we can also sort the list of fruits in reverse order
fruits.sort(reverse=True)
print(fruits)

# we can sort the list temporarily
# mostly for the sake of data visualisation we use the function sorted()
print(sorted(fruits)) #this line makes sure that the list of fruits is temporarilly displayed in sorted form
print(fruits) # Here the list returns to its original form of characteristics

###Printinfg the list in reverse order
#consider the following list
programming_languages = ["Python","C++","Java","C#","Javascript","TypeScript"]
# to print this in reverse order we use the reverse function reverse()
programming_languages.reverse() #Here we commanded the list to be reversed permanently
print(programming_languages)
programming_languages.reverse() #Here we reversed the list to its original form
print(programming_languages)

#### In finding the length of the list we use the same function as used in the string session
# We use the fucton len len()

print(len(programming_languages))
print(len(cars))
print(len(fruits))

#we can make a numerical list by using the range function
#example 
num_to_10 = list(range(0,10))
print(num_to_10)

# we can also convert strings to list by inserting/enclosing/wrapping the object in the list function
string_list = list("Mamayako")
print(string_list)

num_to_20 = list(range(1,21))
print(num_to_20)

# we can use some numerical operation by importing math library
# we can use other mathematical fuctions in the ls=ist too
import math
max_num=max(num_to_20)
min_num=min(num_to_20)
sum_num=sum(num_to_20)

print(max_num)
print(min_num)
print(sum_num)

### Slicing of a list, here we can work with as many sliced parts as we could, even if it means we need
#to store it in a separate variable
#here we will use the fruits list and slice it up into two to store different values of the list

slice1 = fruits[0:3]
print(slice1)
slice2 = fruits[3:5]
print(slice2)
#print(len(fruits))
slice3 = fruits[5:8]
print(slice3)

# we can also copy a list..
# we use the key [:] or the copy method/function copy()
#for example...............# I want slice4 to be equal to the slice3
slice4 = slice3[:]
print(slice4)

slice5 = slice2.copy()
print(slice5)

##Consider the following repetitive list. now we would like to count the number of elements repeting
#in the list using the list_name.count(element)
# consider 
numbers = [2,6,8,2,1,4,6,8,2,3,1,67,8]
print(numbers.count(1)) # this will show how many 2s are present in the list of numbers



