# here we will be discussing about two dimensional lists
# so we can refer to it as a rectangular array of numbers
# consider a matrix example
matrix = [
    [1,2,3],
    [4,5,6],
    [5,6,7]
]

print(matrix)

#now we need to know how to access individual items in the 2d-lists
#in order to access the individual items of the first component of the array, we do as follows
print(matrix[0][1])
print(matrix[1][1])
print(matrix[2][1])

matrix_string = matrix[:]
print(matrix_string)

matrix_string[0][1] = "Gabriel"
matrix_string[0][0] = "Joseph"
matrix_string[0][2] = "Mahembega"
matrix_string[1][1] = "Jaden"
matrix_string[1][0] = "Andrew"
matrix_string[1][2] = "Shimba"
matrix_string[2][1] = "Christina"
matrix_string[2][0] = "Mrigo"
matrix_string[2][2] = "Charles"

print(matrix_string)


# we can basically use nested loops to itterate through all the vcalues in a 2d matrix
# here we ho
for row in matrix:
    for item in row:
        print(item)
