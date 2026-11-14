import math
from cmath import sqrt


def check(x):
    if(x < 2):
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True


n = int(input())
a = map(int, input().split())
a_sorted = list(dict.fromkeys(a))
Sum_pre = 0
Sum_suf = sum(a_sorted)
ans = -1
for i in range(0, len(a_sorted)):
    Sum_pre += a_sorted[i]
    Sum_suf -= a_sorted[i]
    if(check(Sum_suf) and check(Sum_pre)):
        ans = i
        break
if(ans == -1):
    print("NOT FOUND")
else: print(ans)