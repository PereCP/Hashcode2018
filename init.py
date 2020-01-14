class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ride:
    def __init__(self, id, spos, fpos, stime, ftime):
        self.id = id
        self.spos = spos
        self.fpos = fpos
        self.stime = stime
        self.ftime = ftime

    def __lt__(self, other):
        return (self.getViability() < other.getViability())

def distance(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)

def viability(ride1, ride2):
    time = ride2.stime - ride1.ftime
    if (time < 0):
        return 100000
    return distance(ride1.fpos, ride2.spos) + time

#This function returns the time elapsed to complete a car's travel.
def reqtime(car):
    sum = car[0].stime + distance(car[0].spos, car[0].fpos)
    for i in range(1, len(car)):
        if (sum < car[i].stime):
            sum += car[i].stime - sum
        sum += distance(car[i - 1].fpos, car[i].spos) + distance(car[i].spos, car[i].fpos)
    return sum

def most_viable_ride(ride, rides):
    min = 1000000
    best = Ride(0, Point(0, 0), Point(0, 0), 0, 0)
    for x in rides:
        viab = viability(ride, x)
        if (viab < min):
            min = viab
            best = x
    return best

#n: Number of cars.
def sort_by_viability(rides, n):
    origin = Point(0, 0)
    start = Ride(0, origin, origin, 0, 0)
    vtc = [[] for _ in range(n)]
    v = rides.copy()
    for i in range(n):
        current = most_viable_ride(start, rides)
        rides.remove(current)
        vtc[i].append(current)

    while len(rides) > 0:
        maxv = 0
        id = 0
        corresponding = rides[-1]
        for i in range(n):
            myride = most_viable_ride(vtc[i][-1], rides)
            current = viability(vtc[i][-1], myride)
            if (current < maxv):
                maxv = current
                id = i
                corresponding = myride
        vtc[id].append(corresponding)
        rides.remove(corresponding)
    return vtc

def print_cars(vtc):
    for car in vtc:
        print(len(car), end=' ')
        for ride in car:
            print(ride.id, end=' ')
        print()

########## DEBUG ###########
def print_ride(ride):
    print(str(ride.spos.x) + ' ' + str(ride.spos.y) + ' ' + str(ride.fpos.x) + ' '
          + str(ride.fpos.y) + ' ' + str(ride.stime) + ' ' + str(ride.ftime))
############################

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
    ride = Ride(x, pointstart, pointfinish, int(ln[4]), int(ln[5]))
    rides.append(ride)
vtc = sort_by_viability(rides, f)
print(reqtime(vtc[0]))
print(reqtime(vtc[1]))