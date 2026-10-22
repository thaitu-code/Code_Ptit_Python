t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ok = 0
    for j in range(n):
        if(a[j] > b[j]):
            ok = 1
            break
    if(ok == 0):
        print("YES")
    else: print("NO")