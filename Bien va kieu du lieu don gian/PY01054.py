import math


t = int(input())

def sum(n):
    s = 1
    while(n > 0):
        if(n % 10 != 0):
            s = s * (n % 10)
        n//=10
    return s
for i in range(t):
    n = int(input())
    print(sum(n))
