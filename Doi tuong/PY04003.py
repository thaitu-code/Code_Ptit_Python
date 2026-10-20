def gcd(a, b):
    if(b == 0): return a
    return gcd(b, a % b)

class pso:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def Prin(self):
        return f"{self.a}/{self.b}"
    def rutgon(self):
        tmp = gcd(self.a, self.b)
        return pso(int(self.a/tmp), int(self.b/tmp))


a, b = map(int, input().split())
pso1 = pso(a, b)
pso1 = pso1.rutgon()
ans = pso1.Prin()
print(ans)
