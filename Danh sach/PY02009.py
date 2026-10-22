t = int(input())
for i in range(t):
    n = int(input())
    dic = {}
    for j in range(n):
        tmp = int(input())
        if(tmp not in dic):
            dic[tmp] = 1
        else:
            c = dic[tmp]
            c+=1
            dic[tmp] = c
    ans = 0
    cnt = 0
    for a, b in dic.items():
        if(b >= cnt):
            if(b > cnt):
                ans = a
                cnt = b
            elif(a < ans):
                ans = a
    print(ans)

