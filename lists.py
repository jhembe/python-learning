 # in order to write a list, you need to use the following syntax
 # name_of_list = [content1,content2]
#          0      1       2          3
names = ["John","Bob","Gabriel","Gonzales"]
print(names);

# we can specify the index of the specific item in the list
print(names[2]) 
print(names[3])
#we can also use the negative index to define elements in a list
print(names[-2])
print(names[-1])
#we can also print the list of contents of in through the list

print(names[2:])
print(names[2:3])
#we can also put only [:]
print(names[:])

names[0] = "Joseph"
print(names)