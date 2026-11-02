
t = int(input())
for i in range(t):
    n, m, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = []
    i, j, k = 0, 0, 0
    while(i < n and j  < m and k < q):
        if(a[i] == b[j] and b[j] == c[k]):
            ans.append(a[i])
            i+=1
            j+=1
            k+=1
        else:
            tmp = max(a[i], b[j], c[k])
            if(a[i] < tmp):
                i+=1
            if(b[j] < tmp):
                j+=1
            if(c[k] < tmp):
                k+=1
    if(len(ans) == 0):
        print("NO")
    else:
        for char in ans :
            print(char, end = " ")
        print()