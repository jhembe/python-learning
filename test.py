# # x = "5"
# # y = "10"
# # print(x+y)    

# # def sum(x:int,y:int):
# #     print(x+y)


# # sum(3,6)

# # for x in range(0,5):
# #     print(x)
# #     x+=1

# my_dictionary = {
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four",
#     "5":"five",
#     "6":"six",
#     "7":"seven",
#     "8":"eight",
#     "9":"nine",
#     "0":"zero"
# }

# phone_numbers=input("Phone : ")

# output = ""

# for phone in phone_numbers:
#     output += my_dictionary.get(phone,"!")+" "
# print(output)

import utils

numbers = [3,5,1,2,54,2,56,7,13,56,78,9,0]

maximum_number = utils.find_max(numbers)
print(maximum_number)