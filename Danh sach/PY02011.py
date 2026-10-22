n = int(input())
a = list(map(int, input().split()))

cnt = 10**100
ans = -1
for i in range(n):
    tmp = 0
    for j in range(n):
        if(i != j):
            tmp += abs(a[i] - a[j])
    if(tmp < cnt):
        cnt = tmp
        ans = a[i]
print(f"{cnt} {ans}" )
