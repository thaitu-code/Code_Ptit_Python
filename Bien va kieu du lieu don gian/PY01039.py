
def check(n):
    for i in range(0, len(n) - 2, 2):
        if(n[i] != n[i + 2]):
            return False
    for i in range(1, len(n) - 2, 2):
        if(n[i] != n[i + 2]):
            return False
    return True


t = int(input())
for i in range(t):
    s = input()
    if(check(s)):
        print("YES")
    else: print("NO")
