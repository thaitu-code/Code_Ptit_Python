import math

t = int(input())
for i in range(t):
    n = int(input())
    if(n == 1):
        print("1")
    else: print("1 * ", end = "")
    for j in range(2, math.isqrt(n) + 1):
        cnt = 0
        if(n % j == 0):
            while(n % j == 0):
                cnt +=1
                n/=j
            if(n != 1):
                print(f"{int(j)}^{cnt} * ", end = "")
            else: print(f"{int(j)}^{cnt}")
    if(n != 1):
        print(f"{int(n)}^1")

