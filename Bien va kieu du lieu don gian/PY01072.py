n, k = map(int, input().split())
Sett = sorted(list(set(map(int,input().split()))))
# print(Sett)
n = len(Sett)
a = [0] * (k + 1)

def Try(i):
    for j in range(a[i - 1] + 1, n - k + i + 1):
        a[i] = j
        if(i == k):
            for q in range(1, k + 1):
                print(Sett[a[q] - 1], end = " ")
            print()
        else: Try(i + 1)
Try(1)