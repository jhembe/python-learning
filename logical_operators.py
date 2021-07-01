#logical operators
# e.g we are building an application for processing
# #loans,If an applicant has high income and good credit
# #then they are eligible for loan.
# # Here we use the logical operator "and"
# has_high_income=True
# has_good_credit=False
# has_criminal_record = False
# if has_high_income and has_good_credit and not has_criminal_record:
#     print("The user is eligible for loan")
# else :
#     print("The user is not eligible for loan")

# ##using the logical operator "or"

# if has_high_income or has_good_credit and not has_criminal_record:
#     print("The user is eligible for the loan")
# else :
#     print("The user is not eligible for the loan")

####The comparison operator

# temp = int(input("Please enter the temperature to evaluate : "))

# if temp>30:
#     print("It's a hot day ")
# elif temp == 30:
#     print("The temperature is marginal ")
# elif temp<10:
#     print("It's a cold day ")
# else:
#     print("It's neither cold nor hot ")

# nameis ="JOSEPH"
# print(len(nameis))

nameis = input("Please enter to test the compatibility ")

if len(nameis) == 6 :
    print("The length of the name is perfect")
elif len(nameis) > 6 :
    print("The lenght of the name is too much ")
elif len(nameis) < 6 :
    print("The length of the name is too low ")
else :
    print("An error occured" )  
