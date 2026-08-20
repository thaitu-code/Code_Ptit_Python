def check(s):
    if(len(s) < 3):
        return False
    for j in range(len(n)):
        ok = 0
        for l in range(0, j):
            if(s[l] >= s[l + 1]):
                ok = 1
                break
        if(ok == 0):
            for r in range(j + 1, len(n)):
                if(s[r - 1] <= s[r]):
                    ok = 1
                    break
            if(ok == 0):
                return True
    return False

t = int(input())
for i in range(t):
    n = input()
    if(check(n)):
        print("YES")
    else: print("NO")
    

