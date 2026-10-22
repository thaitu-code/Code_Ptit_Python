
f = [0] * 93
f[1] = 1
f[2] = 1
for i in range(3, 93):
    f[i] = f[i - 1] + f[i - 2]

t = int(input())
for i in range(t):
    a, b= map(int, input().split())
    for j in range(a, b + 1):
        print(f"{f[j]} ", end = "")

    print()