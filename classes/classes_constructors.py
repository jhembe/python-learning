# A constructor is a fuction that gets called at a time of creating an object
class Point:
    # NOTE, here i want to create a constructor using the following synatax
    def __init__(self,x,y):
        self.x = x
        self.y = y

point1 =Point(10,5)
# we can also update the values using the following code
point1.y = 18
print(point1.y) 