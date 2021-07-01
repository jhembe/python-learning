#the following programs will be converting the entered value to the opposite one

num = float(input("Enter the number to be converted : "))
option = input(f'(l)bs or (k)gs : ')

if option == "l" or option == "L":
# if option.upper == "L":
    print(f'{num/2.2} kgs')
else :
    print(f'{num*2.2} lbs')