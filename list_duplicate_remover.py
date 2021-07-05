# In this exercise we are going to create a program that removes duplicates

#consider the following repetitive list
list_representative = [ "mama","baba","mama","bibi"]
unique = []

#trying using for loop
#my concept is to itterate through the values and comparing them if they are equal,
#if they are then the index of the repeated one is deleted
# rep = list_repetitive[0]
# for list_rep in list_repetitive:
#     if list_rep == list_rep:
#         del list_repetitive[list_rep]
# print(list_repetitive)

for list_rep in list_representative:
    if list_rep not in unique:
        unique.append(list_rep)

print(unique)