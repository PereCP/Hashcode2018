class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ride:
    def __init__(self, start, finish, times, timee):
        self.start = start
        self.finish = finish
        self.times = times
        self.timee = timee


def distance(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y)
