import math

def check(x):
    if(x < 2):
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True

n, m = map(int, input().split())

for i in range(n):
    a = list(map(int, input().split()))
    for i in range(0, len(a)):
        if(check(a[i])):
            print(1, end = " ")
        else: print(0, end = " ")
    print()


