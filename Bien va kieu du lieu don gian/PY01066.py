t = int(input())
while(t > 0):
    s = input()
    tmp1 = []
    tmp2 = []
    for j in range(1, len(s)):
        tmp1.append(abs(ord(s[j]) - ord(s[j - 1])))
    for j in range(len(s) - 2, -1, -1):
        tmp2.append(abs(ord(s[j]) - ord(s[j + 1])))
    if(tmp1 == tmp2):
        print("YES")
    else: print("NO")
    t-=1