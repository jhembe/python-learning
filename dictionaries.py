# we use dictionaries when we want to store values that are key value pairs
# the following is the syntax example

customer = {
    "name" : "Joseph Gabriel",
    "age" : 30,
    "is_verified" : True
    # NOTE the key values should always be unique, if we add another key value pair within 
    #      we end up getting errors

}

print(customer)

#in order to acces the elements within dictionaries, we use square brackets and then we type the keys
print(customer["age"])
# print(customer["birth"])
#we can also use the get method to acces the dictionary
print(customer.get("name")) # the good thing about this is that if we pass a key that isn't in the dictionary 
                            # it wont bring up an error

customer.get("birthdate","Jan 1 1999")
print(customer.get("birthdate"))

# we can also modify the values of the dictionaries
customer["name"] = "Loistracy"
print(customer)