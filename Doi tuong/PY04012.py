class sinhvien:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.cc = 10
    def count_cc(self, tmp):
        for char in tmp:
            if(char == 'm'):
                self.cc = max(0, self.cc - 1)
            elif(char == 'v'):
                self.cc = max(0, self.cc - 2)
    def Prin(self):
        if(self.cc == 0):
            return f"{self.a} {self.b} {self.c} {self.cc} KDDK"
        else:
            return f"{self.a} {self.b} {self.c} {self.cc}"


t = int(input())
Lis = []
for i in range(t):
    a = input()
    b = input()
    c = input()
    sv = sinhvien(a, b, c)
    Lis.append(sv)
for i in range(t):
    msv, tmp = map(str, input().split())
    for sv in Lis:
        if(sv.a == msv):
            sv.count_cc(tmp)
            break
for sv in Lis:
    print(sv.Prin())


