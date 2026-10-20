import sys


class Rectangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = str(c)

    def perimeter(self):
        if(self.a < 0 or self.b < 0):
            print("INVALID")
            sys.exit(0)
        return (self.a + self.b) * 2
    def area(self):
        return self.a * self.b
    def color(self):
        ans = ""
        for i in range(len(self.c)):
            if(i == 0):
                ans += self.c[i].upper()
            else:
                ans += self.c[i].lower()
        return ans


if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
