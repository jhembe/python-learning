def find_max(numbers):
    max_value = numbers[0]
#lets use the for loop to itterate through the list

    for number in numbers:
        if number > max_value:
            max_value = number
        

    return max_value