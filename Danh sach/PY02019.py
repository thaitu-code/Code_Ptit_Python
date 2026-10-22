def gcd(a, b):
    if(b == 0): return a
    return gcd(b, a % b)

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if(gcd(a[i], a[j]) == 1):
            print(f"{a[i]} {a[j]}")