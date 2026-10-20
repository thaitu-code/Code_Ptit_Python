class thisinh:
    def __init__(self, a, b, c, d, e):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
    def tongdiem(self):
        sum = self.c + self.d + self.e
        return f"{sum:.1f}"
    def Prin(self):
        print(f"{self.a} {self.b} {self.tongdiem()}")
        return None

a = input()
b = input()
c = float(input())
d = float(input())
e = float(input())
ts = thisinh(a, b, c, d, e)
ts.Prin()
