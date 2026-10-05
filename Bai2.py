class Thisinh:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = float(c)
        self.d = float(d)
        self.e = float(e)
    def sum(self):
        return float(self.c + self.d + self.e)
    def Printed(self):
        print(f"{self.a} {self.b} {self.sum():.1f}")

a = input()
b = input()
c = input()
d = input()
e = input()
ts = Thisinh(a, b, c, d, e)
ts.Printed()