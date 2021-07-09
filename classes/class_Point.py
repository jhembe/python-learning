# In class we use naming conventions of camel case
# consider a class Point/ Pascal Naming conventions
# The class defines the blueprint of objects
# NOTE An object is an instance of a class

class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("draw")

#in order to initialize new instance variables we use .....
point1 = Point()
point1.draw()

# NOTE Objects can also have atributes or variables that belong to particular object
point1.x = 10
point1.y = 15

print(point1.x)

point2 = Point()
point2.x =1
point2.y = 6

# print(point2.x)

     

