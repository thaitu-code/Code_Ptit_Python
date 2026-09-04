ans = ['1', '2']
c = ['0', '1', '2']


def check(x):
    cnt = 0
    len_x = 0
    while(x > 0):
        len_x+=1
        tmp = x % 10
        if(tmp == 2): cnt+=1
        x//=10
    if(cnt > len_x // 2):
        return True
    return False

def sinh():
    i = 0
    while(len(ans) < 300000):
        start_point = i
        for j in range(start_point, len(ans)):
            for char in c:
                ans.append(ans[j] + char)
            i+=1
    return 

t = int(input())
sinh()
while(t > 0):
    n = int(input())
    cnt, pos = 0, 0
    while(cnt < n):
        if(check(int(ans[pos]))):
            print(ans[pos], end = " ")
            cnt+=1
        pos+=1
    print()
    t-=1