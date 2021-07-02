#This basically means adding loop within another loop..
#for example, we want to generate a list of continous co-ordinates
# eg (0,0),(0,1),(0,2) etc

for x in range(5):
    for y in range(5):
        print(f'({x},{y})')
    
    