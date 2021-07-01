secret_number =9
gues_count = 0
gues_limit = 3
while gues_count < gues_limit :
    gues = int(input("Enter your gues : "))
    gues_count += 1
    if gues == secret_number:
        print("You won ..")
        break
    else :
        print("you failed")
