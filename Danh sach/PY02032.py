
s = input()
a = set()
for i in range(0, len(s), 2):
    if(i != len(s) - 1):
        tmp = s[i:i + 2]
        a.add(int(tmp))
sorted_a = sorted(list(a))
for x in sorted_a:
    print(x, end = " ")
