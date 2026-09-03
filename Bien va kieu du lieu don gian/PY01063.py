import math


t = int(input())

while(t > 0):
    s = input()
    n = input()
    lenN = len(n)
    ans = 0
    i = 0
    while(i < len(s)):
        tmp = s[i:i + lenN]
        if(tmp == n):
            ans += 1
            i += lenN - 1
        i+=1
    print(ans)
    t-=1