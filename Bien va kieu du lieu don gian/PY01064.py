s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def findKiTu(n, k):
    if(k == pow(2, n - 1)):
        return s[n - 1]
    if(k > pow(2, n - 1)):
        return findKiTu(n - 1, k - pow(2, n - 1))
    else: return findKiTu(n - 1, k)

t = int(input())

while(t > 0):
    n, k = map(int, input().split())
    print(findKiTu(n, k))
    t-=1
# ABACABADABACABA