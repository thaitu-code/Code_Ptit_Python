t = int(input())
for i in range(t):
    n = int(input())
    p = 10
    while(n >= p):
        du = n % p
        if(du >= p // 2):
            n = n - du + p
        else:
            n = n - du
        p*=10
    print(n)