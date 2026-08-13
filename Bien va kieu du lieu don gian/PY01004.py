import math

def snt(x):
    if(x < 2): return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    ok = False
    cnt = 0
    for i in range(1, n):
        if(math.gcd(i, n) == 1): cnt+=1
    if(snt(cnt)): print("YES\n")
    else: print("NO\n")

