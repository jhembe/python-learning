##### Write a python program that finds the largest number in a list

numbers = [5,8,2,1,10,25,3,10]
max_value = numbers[0]
#lets use the for loop to itterate through the list

for number in numbers:
    if number > max_value:
        max_value = number
  

print(max_value)





