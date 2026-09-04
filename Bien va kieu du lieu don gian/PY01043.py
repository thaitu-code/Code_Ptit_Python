q = ['2', '4', '6', '8']
c = ['0', '2', '4', '6', '8']

ans = []
i = 0

while(True):
    if(len(ans) > 0 and int(ans[-1]) > 1000000):
        break
    start_pos = i
    for j in range(start_pos, len(q)):
        tmp = q[j] + q[j][::-1]
        ans.append(tmp)
        i+=1
    for j in range(start_pos, len(q)):
        for char in c:
            q.append(q[j] + char)
t = int(input())
while(t > 0):
    n = int(input())
    for char in ans:
        if(int(char) < n):
            print(char, end = " ")
        else: break
    print()
    t-=1
