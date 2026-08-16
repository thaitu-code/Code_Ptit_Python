import math


t = int(input())

def checksum(n):
    sum = 0
    while(n > 0):
        sum += int(n % 10)
        n/=10
    return sum

def check(n):
    x1 = n % 10
    n//=10
    while(n > 0):
        x2 = n % 10
        if(abs(x1 - x2) != 2):
            
            return False
        x1 = x2
        n//=10
    return True

for i in range(t):
    n = int(input())
    if(checksum(n) % 10 == 0 and check(n)):
        print("YES")
    else: print("NO")