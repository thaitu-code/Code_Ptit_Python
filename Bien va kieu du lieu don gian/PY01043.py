
def check1(n):
    tmp = n[::-1]
    return tmp == n
def check2(n):
    for i in n:
        if(int(int(i)) % 2 == 1): return False
    return True
def check3(n):
    return len(n) % 2 == 0

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(22, n, 2):
        s = str(j)
        if(check3(s) and check1(s) and check2(s) ):
            print(j, end = " ") 
    print()