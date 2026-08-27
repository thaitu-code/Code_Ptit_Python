import math

def checksnt(n):
    if(n < 2): return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0): return False
    return True
def check1(n):
    if(checksnt(len(n))):
        return True
    return False
def check2(n):
    cnt1, cnt2 = 0, 0
    for char in n:
        if(checksnt(int(char))):
            cnt1+=1
        else: cnt2+=1
    return cnt1 > cnt2

t = int(input())
for i in range(t):
    n = input()
    if(check1(n) and check2(n)):
        print("YES")
    else: print("NO")