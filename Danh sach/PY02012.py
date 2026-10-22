import sys

n = int(input())
a = sys.stdin.read().split()
if(a):
    chan = []
    le = []
    pos = [""] * n
    for i in range(len(a)):
        if(int(a[i]) % 2 == 0):
            pos[i] = "chan"
            chan.append(int(a[i]))
        else:
            pos[i] = "le"
            le.append(int(a[i]))
    chan.sort()
    le.sort(reverse=True)
    l, r = 0, 0
    for i in range(n):
        if(pos[i] == "chan"):
            print(chan[l], end=" ")
            l+=1
        else:
            print(le[r], end=" ")
            r+=1
