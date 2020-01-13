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

    def __lt__(self, other):
        return (self.getViability() < other.getViability())

    # As smaller the number is the ride is more viable.
    def getViability(self):
        return (distance(self.spos, self.fpos) / (self.ftime - self.stime))

def distance(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)

# Read file
arxiu = open("a_example.in")
# first line
l1 = arxiu.readline()
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
    ln = arxiu.readline()
    ln = ln.replace('\n', '')
    ln = ln.split(' ')
    # row = x
    # column = y
    pointstart = Point(int(ln[0]), int(ln[1]))
    pointfinish = Point(int(ln[2]), int(ln[3]))
    ride = Ride(pointstart, pointfinish, int(ln[4]), int(ln[5]))
    rides.append(ride)
rides.sort()
for x in rides:
    print(x.spos.x + ' ' + x.spos.y + ' , ' + x.fpos.x + x.fpos.y)