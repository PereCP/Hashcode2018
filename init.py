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


def distance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)
