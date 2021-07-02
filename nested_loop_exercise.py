number_stars = [2,2,2,2,6]

for output in number_stars:
    print("X"*output)
print("\n")


# Let's imagine we have to use an inner_loop
for x_count in number_stars:
    output = ""
    for count in range(x_count):
        output += "x"
    print(f'{output}')

