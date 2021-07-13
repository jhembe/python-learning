#here is the app to add and remove users in an 

#creating an array of names
#implementing switch statements

names_array = []
user_input = ""
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



while user_input.lower() != "quit":
    user_input = input("> ")
    if user_input.lower() == "add":
        add_people()
    elif user_input.lower() == "del":
        del_people()
    elif user_input.lower() == "help":
        print('''
        add  - To add users
        del  - TO delete users
        quit - TO exit the program
        ''')
    elif user_input.lower() == "quit":
        exit()
    else :
        print("I dont understand yout input")


