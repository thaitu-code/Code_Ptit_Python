import math


t = int(input())

def check(s):
    n = int(s)
    if(n < 2):
        return False
    for i in range(2, int(math.sqrt(n))):
        if(n % i == 0):
            return False
    return True

for i in range(t):
    n = input()
    s = max(0, len(n) - 4)
    s1 = n[s:]
    if(check(s1)):
        print("YES")
    else: print("NO")
