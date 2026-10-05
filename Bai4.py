class sinhvien:
    def __init__(self, masv, hoten, ml):
        self.masv = masv
        self.hoten = hoten
        self.ml = ml
        self.score = 0
    def abs_check(self, x):
        diem = 10
        for i in x:
            if(i == 'm'):
                diem = max(0, diem - 1)
            elif(i == 'v'):
                diem = max(0, diem - 2)
        return diem
    def Printed(self):
        print(f"{self.masv} {self.hoten} {self.ml} {self.score} ", end="")
        if(self.score == 0):
            print("KDDK")
        print("\n")

t = int(input())
ds_sinhvien = []
for i in range(t):
    a = input()
    b = input()
    c = input()
    ds_sinhvien.append(sinhvien(a, b, c))
for i in range(t):
    a = input().split()
    for sv in ds_sinhvien:
        if(sv.masv == a[0]):
            sv.score = sv.abs_check(a[1])
            break
for sv in ds_sinhvien:
    sv.Printed()



