import math

t = int(input())
for i in range(t):
    n = int(input())
    x1, x2 = n, 0
    while(n > 0):
        x2 = x2 * 10 + n % 10
        n//=10
    if(math.gcd(x1, x2) == 1):
        print("YES")
    else: print("NO")
    