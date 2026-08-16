import math


x1, x2 = map(int, input().split())
for i in range(x1, x2 - 1):
    for j in range(i + 1, x2):
        for k in range(j + 1, x2 + 1):
            if(math.gcd(i, j) == 1):
                if(math.gcd(j, k) == 1):
                    if(math.gcd(i, k) == 1):
                        print(f"({i}, {j}, {k})")