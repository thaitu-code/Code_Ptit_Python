
a, b, m = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    tmp = bin(i)[2:]
    if(tmp != tmp[::-1]):
        continue
    ok = 1
    tmp1 = i
    for j in range(3, m + 1):
        i = tmp1
        tmp = []
        if(i < j):
            continue
        while(i > 0):
            x = i % j
            tmp.append(x)
            i//=j
        if(tmp != tmp[::-1]):
            ok = 0
            break
    if(ok ==1 ):
        cnt+=1
print(cnt)



