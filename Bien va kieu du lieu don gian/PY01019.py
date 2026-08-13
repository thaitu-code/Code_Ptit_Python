t = int(input())
for i in range(t):
    s1 = input()
    s2 = s1[::-1]
    s1.split()
    s2.split()
    ok = False
    if(len(s1) <= 1):
        print("YES")
        continue
    for i in range(1, len(s1)):
        if(abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1]))):
            ok = True
            break
    if(ok): print("NO")
    else: print("YES")