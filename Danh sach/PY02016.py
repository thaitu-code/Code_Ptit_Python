t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    target = n // 2
    dic = {}
    for char in a:
        if(char not in dic):
            dic[char] = 1
        else:
            dic[char] = dic[char] + 1
    ok = 0
    for ke, val in dic.items():
        if(val > target):
            print(ke)
            ok = 1
            break
    if(ok == 0):
        print("NO")