s = input()
s.split()
ans = 0
for i in range(len(s)):
    if(s[i] == '4' or s[i] == '7'):
        ans+=1
if(ans == 4 or ans == 7):
    print("YES")
else: print("NO")