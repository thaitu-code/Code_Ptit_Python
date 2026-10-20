class tram:
    def __init__(self, ten, st, en, lm):
        self.ma = ""
        self.ten = ten
        self.st = st
        self.en = en
        self.time = 0
        self.lm = lm
    def time_init(self):
        a, b = map(int, self.st.split(":"))
        c, d = map(int, self.en.split(":"))
        tmp = 0
        if(d < b):
            c-=1
            tmp += (c - a) * 60 + 60 + d - b
        else:
            tmp += (c - a) * 60 + d - b
        return tmp
    def add_time(self, tramtmp):
        self.time += tramtmp.time_init()
    def add_lm(self, tramtmp):
        self.lm += tramtmp.lm
    def vantoc(self):
        cnt = float(float(self.lm)/(self.time / 60))
        return f"{cnt:.2f}"


Dic={}
t = int(input())
for i in range(t):
    a = input()
    b = input()
    c = input()
    d = float(input())
    tramtmp = tram(a, b, c, d)
    if(a not in Dic):
        tramtmp.time = tramtmp.time_init()
        Dic[a] = tramtmp
    else:
        tmp = Dic[a]
        tmp.add_time(tramtmp)
        tmp.add_lm(tramtmp)
cnt = 1
for a in Dic:
    ans = Dic[a].vantoc()
    print(f"T0{cnt} {Dic[a].ten} {ans}")
    cnt+=1

