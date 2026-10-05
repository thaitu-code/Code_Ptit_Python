t = int(input())

class sophuc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Printed(self, sp1):
        if(self.b > 0 and sp1.b > 0):
            print(f"{self.a} + {self.b}i, {sp1.a} + {sp1.b}i\n")
        elif(self.b > 0 and sp1.b < 0):
            print(f"{self.a} + {self.b}i, {sp1.a} - {sp1.b * -1}i\n")
        elif(self.b <  0 and sp1.b > 0):
            print(f"{self.a} - {self.b * -1}i, {sp1.a} + {sp1.b}i\n")
        else:
            print(f"{self.a} - {self.b * -1}i, {sp1.a} - {sp1.b* -1}i\n")
def sum(sp1, sp2):
    a1 = sp1.a + sp2.a
    a2 = sp1.b + sp2.b
    ans = sophuc(a1, a2)
    return ans

def multiply(sp1, sp2):
    a1 = sp1.a * sp2.a - sp1.b * sp2.b
    a2 = sp1.b * sp2.a + sp1.a * sp2.b
    ans = sophuc(a1, a2)
    return ans

for i in range(t):
    a, b, c, d = map(int, input().split())
    sp1 = sophuc(a, b)
    sp2 = sophuc(c, d)
    C = multiply(sum(sp1, sp2), sp1)
    D = multiply(sum(sp1, sp2), sum(sp1, sp2))
    C.Printed(D)

# (a + bi)(c + di) = ac -bd + (bc + ad)i