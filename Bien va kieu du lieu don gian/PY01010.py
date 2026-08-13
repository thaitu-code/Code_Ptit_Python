t = int(input())
for i in range(t):
    n = input()
    s1 = n[0: 2]
    s2 = n[len(n) - 2:]
    if(s1 == s2): print("YES")
    else: print("NO")