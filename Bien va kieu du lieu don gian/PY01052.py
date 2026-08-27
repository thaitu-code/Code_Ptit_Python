import math


t = int(input())

def sum(n):
    s = 0
    while(n > 0):
        s += n % 10
        n//=10
    return s
def check(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True
for i in range(t):
    n = int(input())
    s = sum(n)
    if(check(s)):
        print("YES")
    else: print("NO")
