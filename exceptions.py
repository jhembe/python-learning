#NOTE Here is how to handle error exceptions in Python programming language
#     Here is where we can avoid to the program to crash with error code 1

try:
    age =int(input("Age : "))
    income = 20000
    risk = income/age               
    print(age)
except ZeroDivisionError:           # This is the exception block for the error ZeroDivision
    print("You cannot devide by zero")
except ValueError:              # This is the exception block for the error ValueError
    print("Invalid value,You should use integers only")
                            
