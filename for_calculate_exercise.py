#the program to calculate the total cost of all the products in the shop
#i'm going to make a list of all the items in a list form, then i'll use a for loop
#to itterate through the list and adding the items

prices = [2000,6000,1200,34000]
total_price = 0

for price in prices:
    total_price = total_price + price

print(f'The total price is : {total_price}')