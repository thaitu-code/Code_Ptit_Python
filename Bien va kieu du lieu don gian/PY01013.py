import math

def check(x):
    if x < 2: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0): return False
    return True
def tong(x):
    sum = 0
    while(x > 0):
        sum += x%10
        x//=10
    return sum

t = int(input())
for i in range(t):
    x1, x2 = map(int, input().split())
    ucln = math.gcd(x1, x2)
    sum = tong(ucln)
    # print(sum)
    if(check(sum)):
        print("YES")
    else: print("NO")
    
