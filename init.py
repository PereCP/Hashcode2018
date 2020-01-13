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

class Car:
    def __init__(self, rides):
        self.rides = rides

    def totalViability(self):
        sum = 0
        for x in self.rides:
            sum += x.getViability()
        return sum

def distance(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)

def viability(ride1, ride2):
    return (distance(ride2.spos, ride1.fpos) + (ride1.ftime - ride2.stime))

def most_viable_ride(ride, rides):
    min = 1000000
    best = Ride(Point(0, 0), Point(0, 0), 0, 0)
    for x in rides:
        viab = viability(ride, x)
        if (viab < min):
            min = viab
            best = x
    return best

def sort_by_viability(rides):
    origin = Point(0, 0)
    ini = Ride(origin, origin, 0, 0)
    best = most_viable_ride(ini, rides)
    v = []
    v.append(best)
    rides.remove(best)
    reference = rides.copy()
    for x in reference:
        best = most_viable_ride(x, rides)
        v.append(best)
        rides.remove(best)
    return v


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
rides = sort_by_viability(rides)
for x in rides:
    print(str(x.spos.x) + ' ' + str(x.spos.y) + ' , ' + str(x.fpos.x) + ' ' +  str(x.fpos.y))