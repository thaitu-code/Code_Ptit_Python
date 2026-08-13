import math
t = int(input())
for i in range(t):
    s = input()
    ans = ""
    num = 0
    for char in s:
        if char.isalpha():
            ans += char
        else: num += int(char)
    s_sorted = "".join(sorted(ans))
    s_sorted += str(num)
    print(s_sorted)