import math


t = int(input())

def check(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            return False
    return True

def check1(n):
    cnt1, cnt2 = 0, 0
    for char in n:
        if(check(int(char))):
            cnt1+=1
        else: cnt2+=1
    return cnt1 > cnt2

while(t > 0):
    n = input()
    x = len(n)
    if(check(x) and check1(n)):
        print("YES")
    else: print("NO")
    t-=1