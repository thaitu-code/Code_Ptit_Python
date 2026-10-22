import math

prime = [0] * 1000002
prime_tmp = []

def ktao():
    for i in range(1, 1000001):
        prime[i] = 1
    prime[1] = prime[0] = 0
    for i in range(2, int(math.sqrt(1000000)) + 1):
        if(prime[i] == 1):
            for j in range(i * i, 1000001, i):
                prime[j] = 0
    for i in range(2, 1000001):
        if(prime[i]):
            prime_tmp.append(i)
ktao()
n, x = map(int, input().split())
cnt = 0
for i in range(0, n + 1):
    print(x, end=" ")
    x += prime_tmp[cnt]
    cnt+=1
