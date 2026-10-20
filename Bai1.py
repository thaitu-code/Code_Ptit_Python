n = int(input())
mon = {'A': 'TOAN', 'B': 'LY', 'C': 'HOA'}
uu = {'1': 2.0, '2': 1.5, '3': 1.0, '4': 0.0}
ds = []
for i in range(n):
    ten = input().strip()
    ma = input().strip()
    tin = float(input())
    cm = float(input())
    tong = tin * 2 + cm + uu[ma[1]]
    kq = "TRUNG TUYEN" if tong >= 18 else "LOAI"
    ds.append(("GV%02d" % (i + 1), ten, mon[ma[0]], tong, kq))

ds.sort(key=lambda x: -x[3])

for g in ds:
    print(g[0], g[1], g[2], "%.1f" % g[3], g[4])