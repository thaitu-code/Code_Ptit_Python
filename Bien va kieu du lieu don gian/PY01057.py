import math


t = int(input())

def check_indx(x):
    if(x < 2):
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0): return False
    return True

def snt(x):
    if(x == 2 or x == 3 or x == 5 or x == 7):
        return True
    return False

def check(n):
    s = str(n)
    for i in range(0, len(s)):
        if(check_indx(i) and snt(int(s[i])) != True):
            return False
        elif(check_indx(i) == False and snt(int(s[i]))):
            return False
    return True
for i in range(t):
    n = int(input())
    if(check(n)):
        print("YES")
    else: print("NO")
