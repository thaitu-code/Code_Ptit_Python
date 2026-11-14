import math

def check(x):
    if(x < 2): return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i  == 0):
            return False
    return True

dic = {}

n = int(input())
Lis = [int(x) for x in input().split()]

for i in range(0, len(Lis)):
    if(check(Lis[i])):
        if(Lis[i] not in dic):
            dic[Lis[i]] = 1
        else:
            dic[Lis[i]] += 1
for key, val in dic.items():
    print(f"{key} {val}")