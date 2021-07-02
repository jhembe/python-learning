##we need to use while loops

user_input = ""

while user_input.lower() != "quit":
    user_input = input("> ")
    if user_input.lower() == "start":
        print("The car started ")
    elif user_input.lower() == "stop":
        print("The car stoped")
    elif user_input.lower() == "help":
        print('''
        start - To start the car
        Stop  - TO stop the car
        quit  - TO exit the game
        ''')
    elif user_input.lower() == "quit":
        exit()
    else :
        print("I dont understand yout input")