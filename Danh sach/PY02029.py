import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
Dic = {}
Min = 1000000

for x in a:
    if(x not in Dic):
        Dic[x] = 1
    else: Dic[x] = Dic[x] + 1

levels = sorted(set(Dic.values()), reverse=True)
if(len(levels) <= 1):
    print("NONE")
    sys.exit()
target = levels[1]
tmp = []
for key, val in Dic.items():
    if(val == target):
        tmp.append(key)
print(min(tmp))