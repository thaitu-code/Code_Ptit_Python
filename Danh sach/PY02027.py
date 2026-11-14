import re

n = int(input())
Lis = []
for i in range(n):
    x = input()
    words = re.findall(r'[0-9]+', x)
    for x in words:
        Lis.append(int(x))
Lis.sort()
for x in Lis:
    print(x)
