import math
from cmath import sqrt
from decimal import Decimal


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def distance(self, p):
        ans = math.sqrt((self.a - p.a) * (self.a - p.a) + (self.b - p.b) * (self.b - p.b))
        return f"{ans:.4f}"

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1