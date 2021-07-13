def find_max(numbers):
    max_value = numbers[0]
#lets use the for loop to itterate through the list

    for number in numbers:
        if number > max_value:
            max_value = number
        

    return max_value

def add_people():
    num_people = int(input("Enter the number of people you want to add : "))

    for person in range(num_people):
        new_name = str(input(" > "))
        names_array.append(new_name)

    print(f'The people in the list are : {names_array}')
def del_people():
    num_people = input("Enter the name of the user you wish to delete : ")
    names_array.remove(num_people)
    print(f'The people in the list are : {names_array}')