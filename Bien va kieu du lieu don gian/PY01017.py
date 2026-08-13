t = int(input())
for i in range(t):
    x = input()
    x.split()
    cnt = 1
    for j in range(1, len(x)):
        if(x[j] != x[j - 1]):
            print(cnt, end="")
            print(x[j - 1], end = "")
            cnt = 1
        else: cnt += 1
    print(cnt, end="")
    print(x[len(x) - 1], end = "")
    print("")