t = int(input())
for i in range(t):
    s = input()
    s1 = s[len(s)-2:]
    # print(s1)
    if(s1 == "86"):
        print("YES")
    else: print("NO")