from datetime import datetime

gia = {1: 25, 2: 34, 3: 50, 4: 80}

lines = [l.strip() for l in open(0).read().split('\n') if l.strip()]
n = int(lines[0])
ds = []
for i in range(n):
    ten = lines[1 + i * 5]
    phong = lines[2 + i * 5]
    d1 = datetime.strptime(lines[3 + i * 5], "%d/%m/%Y")
    d2 = datetime.strptime(lines[4 + i * 5], "%d/%m/%Y")
    dv = int(lines[5 + i * 5])
    ngay = (d2 - d1).days + 1
    tang = int(phong[0])
    tong = ngay * gia[tang] + dv
    ds.append(("KH%02d" % (i + 1), ten, phong, ngay, tong))

ds.sort(key=lambda x: -x[4])
for m, t, p, ng, tong in ds:
    print(m, t, p, ng, tong)