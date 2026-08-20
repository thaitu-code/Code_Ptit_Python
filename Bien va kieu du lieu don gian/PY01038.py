def reverse_num(n):
    n1 = 0
    while(n > 0):
        n1 = n1 * 10 + n %10
        n//=10
    return n1

t = int(input())
for i in range(t):
    cnt = 1000
    n = int(input())
    ok = 0
    while(cnt > 0):
        if(n % 7 == 0):
            print(n)
            ok = 1
            break
        n1 = reverse_num(n)
        n += n1
        cnt-=1
    if(ok == 0): print(-1)
    

