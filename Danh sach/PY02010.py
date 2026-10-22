
while(True):
    n = int(input())
    if(n == 0):
        break
    Min = 10**100 + 1
    Max = -1
    for i in range(n):
        x = int(input())
        Min = min(Min, x)
        Max = max(Max, x)
    if(Min == Max):
        print("BANG NHAU")
    else:
        print(f"{Min} {Max}")
