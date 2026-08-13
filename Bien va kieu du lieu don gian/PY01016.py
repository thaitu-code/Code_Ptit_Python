t = int(input())
for i in range(t):
    x = input()
    x.split()
    for j in range(1, len(x), 2):
        for k in range(int(x[j])):
            print(x[j - 1], end = "")
    print("")