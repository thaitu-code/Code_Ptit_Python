a, k, n = map(int, input().split())
x = (a + k - 1) // k
tmp = x * k - a
if(tmp == 0): tmp += k
ok = True
while(tmp + a <= n):
    ok = False
    if(tmp > 0): print(tmp, end = " ")
    tmp += k
if(ok): print(-1)