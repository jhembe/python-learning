#I'm going to write a simple program that tells the user 
# about the weather condition and provides suggestion on 
# what should be weared or otherwise

##using if_else control flow.

#defining a variable..
# is_cold = True
# is_hot = False


# if is_cold:
#     print("It's a cold day, please wear warm clothes ..")
# elif is_hot:
#     print("It's a hot day, drink plenty of water ..")
# else:
#     print("It's a perfect day, have fun today")

####Exercise
#Price of the house is  $1M
#if buyer has good credit,
#   they need to put down 10%
#Otherwise
#   They need to put down 20%
#print the down payement
#

#initializing a necesary variable:
house_price = 1000000
credit_Status =input("Do you have a good credit to buy a house ? (Y/N)")

if credit_Status == "Y" or "y":
    payement = f'The payement is ${0.1*house_price}'
    print(payement)
else :
    print(f'The payement is ${0.2*house_price}')