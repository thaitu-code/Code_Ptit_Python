import math


t = int(input())
def sum(n):
    s = 0
    while(n > 0):
        s += n % 10
        n//=10
    return s
def check3(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True
def check1(n):
    s = str(n)
    for i in range(0, len(s), 2):
        if(int(s[i]) % 2 != 0):
            return False
    return True

def check2(n):
    s = str(n)
    for i in range(1, len(s), 2):
        if(int(s[i]) % 2 != 1):
            return False
    return True
for i in range(t):
    n = int(input())
    if(check1(n) and check2(n) and check3(sum(n))):
        print("YES")
    else: print("NO")
