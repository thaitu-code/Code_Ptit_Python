import math

prime = [1] * 11000
prime_tmp = []

def sang():
    prime[1] = 0
    for i in range(2, int(math.sqrt(11000)) + 1):
        if(prime[i] == 1):
            for j in range(i * i, 11000, i):
                prime[j] = 0
    for i in range(1, 11000):
        if(prime[i] == 1):
            prime_tmp.append(i)

n = int(input())
a = list(map(int, input().split()))
sang()
ans = 0
for i in range(len(a)):
    cnt = 10**100
    l = 0
    r = len(prime_tmp) - 1
    while(l <= r):
        m = (l + r) // 2
        if(prime_tmp[m] == a[i]):
            cnt = 0
            break
        elif(prime_tmp[m] > a[i]):
            r = m - 1
            cnt = min(cnt, abs(prime_tmp[m] - a[i]))
        else:
            l = m + 1
            cnt = min(cnt, abs(prime_tmp[m] - a[i]))
    ans = max(ans, cnt)
print(ans)