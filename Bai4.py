from datetime import datetime

n, m = map(int, input().split())
monhoc = {}
for i in range(n):
    ma = input().strip()
    ten = input().strip()
    monhoc[ma] = ten

lichthi = []
for i in range(1, m + 1):
    ma, ngay, gio , nhom = input().split()
    d = datetime.strptime(ngay, "%d/%m/%Y")
    g = datetime.strptime(gio, "%H:%M")
    lichthi.append((d, g, ma, i, ngay, gio,nhom))
lichthi.sort(key = lambda x:(x[0], x[1], x[2]))
for d, g, ma, i, ngay, gio, nhom in lichthi:
    print(f"T{i:03d} {ma} {monhoc[ma]} {ngay} {gio} {nhom}")