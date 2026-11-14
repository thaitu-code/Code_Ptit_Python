n, m = map(int, input().split())
a = sorted(set(map(int, input().split())))
b = sorted(set(map(int, input().split())))

for x in a:
    if(x in b):
        print(x, end=" ")
print()
for x in a:
    if(x not in b):
        print(x, end = " ")
print()
for x in b:
    if(x not in a):
        print(x, end = " ")
