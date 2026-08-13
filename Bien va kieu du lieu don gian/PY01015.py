t = int(input())
for i in range(t):
    x = input()
    x.split
    ok = True
    for i in range(1, len(x)):
        if(x[i] < x[i - 1]):
            ok = False
            break
    if(ok): print("YES")
    else: print("NO")