n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if(a[j] < a[i]):
            cnt += 1
print(cnt)