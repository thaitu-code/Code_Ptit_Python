s = input()
s.split()
cnt = 0
ans = ""
for i in range(len(s) - 1, 0, -1):
    if(cnt == 2):
        
        ans += s[i]
        ans += ","
        cnt = 0
    else:
        ans += s[i]
        cnt +=1
ans += s[0]
ans = ans[::-1]
print(ans)