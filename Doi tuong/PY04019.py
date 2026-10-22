class nvien:
    def __init__(self, a, b, c):
        self.tt = 0
        self.a = a
        self.b = b
        self.c = c
        self.tb = 0
    def chuan(self):
        if(self.b > 10):
            self.b /= 10
        if(self.c > 10):
            self.c /= 10
    def tbinh(self):
        self.chuan()
        self.tb = (self.b + self.c) / 2


n = int(input())
Lis = []
for i in range(n):
    a = input()
    b = float(input())
    c = float(input())
    nv = nvien(a, b, c)
    nv.tbinh()
    nv.tt = i + 1
    Lis.append(nv)
Lis.sort(key = lambda x : x.tb, reverse=True)
for i in range(len(Lis)):
    if(Lis[i].tt >= 10):
        print(f"TS{Lis[i].tt}", end="")
    else:
        print(f"TS0{Lis[i].tt}", end="")
    print(f" {Lis[i].a} {Lis[i].tb:.2f} ", end="")
    if(Lis[i].tb < 5):
        print("TRUOT")
    elif(Lis[i].tb < 8):
        print("CAN NHAC")
    elif(Lis[i].tb <= 9.5):
        print("DAT")
    else:
        print("XUAT SAC")

