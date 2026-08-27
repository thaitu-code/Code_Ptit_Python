import math

def checksnt(num):
    if(num < 2): return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if(num % i == 0): return False
    return True
def check(n):
    num = int(n[len(n) - 4:])
    # print(num)
    if(checksnt(num)): return True
    return False


t = int(input())
for i in range(t):
    n = input()
    if(check(n)):
        print("YES")
    else: print("NO")