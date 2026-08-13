import sys


P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
P.split()

for line in sys.stdin:
    parts = line.strip().split()
    if(parts[0] == "0"): break
    k = int(parts[0])
    s = parts[1]
    ans = ""
    for char in s:
        original_indx = P.index(char)
        new_indx = (original_indx + k) % 28
        ans += P[new_indx]
    ans = ans[::-1]
    print(ans)