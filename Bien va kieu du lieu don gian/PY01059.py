t = int(input())

def chan(n):
    sum = 0
    for i in range(0, len(n), 2):
        sum += int(n[i])
    return sum
def le(n):
    tich = 1
    ok = 0
    for i in range(1, len(n), 2):
        if(int(n[i]) != 0):
            ok = 1
            tich *= int(n[i])
    if(ok == 0):
        return 0
    return tich

for i in range(t):
    n = input()
    print(f"{chan(n)} {le(n)}")