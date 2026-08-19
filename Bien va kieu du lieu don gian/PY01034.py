import sys

def swap(n, i, j):
    tmp = list(n)
    tmp[i], tmp[j] = tmp[j], tmp[i]
    return "".join(tmp)

t = int(input())

for i in range(t):
    s = input()
    j = len(s) - 2
    tmp = "0"
    while(j >= 0 and s[j] <= s[j + 1]): j-=1
    if(j == -1):
        print(-1)
        continue
    pos = j + 1
    for k in range(len(s) - 1, j, -1):
        if(s[k] < s[j]):
            if(s[k] >= tmp):
                tmp = s[k]
                pos = k
    ans = swap(s, j, pos)
    if(ans[0] == '0'):
        print(-1)
    else:  print(ans)

