t = int(input())
for i in range(t):
    n = int(input())
    if(n % 2 == 0):
        ans = 0
        for j in range(2, n + 1, 2):
            ans += 1/j
    else:
        ans = 0
        for j in range(1, n + 1, 2):
            ans += 1/j
    print(f"{ans:.6f}")
