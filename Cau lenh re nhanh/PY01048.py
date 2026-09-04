t = int(input())
for i in range(t):
    n = int(input())
    k = 2
    cnt = 0
    while(True):
        tmp = n - k*(k-1)/2
        if(tmp <= 0): break
        if(tmp % k == 0):
            cnt+=1
        k+=1
    print(cnt)
