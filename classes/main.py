#classes
#classes can be used to define types
# egs are we can create shopping cart and other real world items as class

class Point:
    def move(self):
        print("Move")
    
    def draw(self):
        print("Draw")

point1 = Point()

point1.draw()
point1.x = 10
point1.y = 20

print(point1.x)
print(point1.y)
