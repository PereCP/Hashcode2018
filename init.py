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
