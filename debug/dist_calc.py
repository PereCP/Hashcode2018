class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)

p1 = Point(0, 0)
print("Enter point 1 values:")
p1.x = int(input("x: "))
p1.y = int(input("y: "))
p2 = Point(0, 0)
print("Enter point 2 values:")
p2.x = int(input("x: "))
p2.y = int(input("y: "))
print("The distance between the points is: " + str(distance(p1, p2)))