class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ride:
    def __init__(self, spos, fpos, stime, ftime):
        self.spos = spos
        self.fpos = fpos
        self.stime = stime
        self.ftime = ftime

def distance(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)


# Read file
f = open("a_example.in")
# first line
l1 = f.readline()
l1 = l1.replace('\n', '')
l1 = l1.split(' ')
r = int(l1[0])
c = int(l1[1])
f = int(l1[2])
n = int(l1[3])
b = int(l1[4])
t = int(l1[5])
rides = []
for x in range(n):
    ln = f.readline()
    ln = ln.replace('\n', '')
    ln = ln.split(' ')
    # row = x
    # column = y
    pointstart = Point(ln[0], ln[1])
    pointfinish = Point(ln[2], ln[3])
    ride = Ride(pointstart, pointfinish, ln[4], ln[5])
    rides.append(ride)
