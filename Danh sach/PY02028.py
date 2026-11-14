import math


def check(x):
    if(x < 2): return False

    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
Lis = []
for x in a:
    if(check(x)):
        Lis.append(x)
Lis.sort()
i = 0
for j in range(n):
    if(a[j] in Lis):
        print(Lis[i] ,end= " ")
        i+=1
    else:
        print(a[j], end = " ")

