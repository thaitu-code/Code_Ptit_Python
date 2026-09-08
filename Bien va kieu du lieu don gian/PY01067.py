from collections import deque

ans = []
def sinh():
    dq = deque(['1', '2'])
    c = ['0', '1', '2']
    
    while(len(ans) < 1000):
        x = dq.popleft()
        if(x.count('2') > len(x) // 2):
            ans.append(x)
        for char in c:
            dq.append(x + char)
    return 

t = int(input())
sinh()
while(t > 0):
    n = int(input())
    for i in range(n):
        print(ans[i], end = " ")
    print()
    t-=1