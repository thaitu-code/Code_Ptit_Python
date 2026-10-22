import math
from cmath import sqrt

import sys


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def canh(self, tmp):
        return math.sqrt((self.a - tmp.a) * (self.a - tmp.a) + (self.b - tmp.b) *(self.b - tmp.b))

class Triangle:
    def __init__(self, c1, c2, c3):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
    def chuvi(self):
        return self.c1 + self.c2 + self.c3

data = sys.stdin.read().split()
if(data):
    t = int(data[0])
    indx = 1
    for i in range(t):
        c1 = Point(float(data[indx]), float(data[indx + 1]))
        c2 = Point(float(data[indx + 2]), float(data[indx + 3]))
        c3 = Point(float(data[indx + 4]), float(data[indx + 5]))
        indx += 6
        d1 = c1.canh(c2)
        d2 = c2.canh(c3)
        d3 = c3.canh(c1)
        if(d1 +  d2 <= d3 or d2 + d3 <= d1 or d1 + d3 <= d2):
            print("INVALID")
            continue
        tri = Triangle(d1, d2, d3)
        print(f"{tri.chuvi():.3f}")