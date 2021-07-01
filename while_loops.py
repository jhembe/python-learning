# we use while loop to execute a block of code multiple times 
  # Its mostly used in making an interactive programs such as games

#syntax
# from multiprocessing import Condition
# from pyexpat.errors import codes


# while Condition:
#     block of codes

i = 1

while i <= 10:
    print("*"*i)
    i=i+1
print("Done\n")

m = 5
while m >= 0:
    print(f"I'm drawing back by {m}")
    m=m-1
print("I'm done")