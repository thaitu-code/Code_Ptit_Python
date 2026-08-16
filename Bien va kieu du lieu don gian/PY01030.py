import math

n, k = map(int, input().split())
i = pow(10, k - 1)
j = pow(10, k)
cnt = 0
for q in range(i, j):
    if(math.gcd(n, q) == 1):
        if(cnt < 9):
            print(q, end = " ")
            cnt += 1
        else:
            cnt = 0
            print(q)