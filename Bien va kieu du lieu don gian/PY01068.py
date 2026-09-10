
n, k = map(int, input().split())
x = input().split()
Sett = sorted(set(x))
n = len(Sett)
a = [0] * (k + 1)
def quay(i):
    for j in range(a[i - 1] + 1, n - k + i + 1):
        a[i] = j
        if(i == k):
            for q in range(1, k + 1):
                print(Sett[a[q] - 1], end = " ")
            print()
        else: quay(i + 1)
quay(1)
