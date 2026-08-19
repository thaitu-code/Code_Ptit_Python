s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    ans_reverse = ""
    while(a > 0):
        x = a % b
        # print(x)
        a //=b
        ans_reverse += s[x]
    ans = ans_reverse[::-1]
    print(ans)
