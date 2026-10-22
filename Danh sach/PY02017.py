t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for char in a:
        if(char not in dic):
            dic[char] = 1
        else:
            dic[char] = dic[char] + 1
    for ke, val in dic.items():
        if(val % 2 == 1):
            print(ke)
            break