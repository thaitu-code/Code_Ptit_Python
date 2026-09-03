import math


t = int(input())

def check(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

while(t > 0):
    n = input()
    x1 = n[:3]
    x2 = n[-3:]
    if(check(int(x1)) and check(int(x2))):
        print("YES")
    else: print("NO")
    t-=1