n = int(input())

tmp = [2, 3, 5, 7]
a = [0] * (n + 1)
def check1():
    if(2 not in a or 3 not in a or 5 not in a or 7 not in a):
        return False
    return True
def check2(length):
    if(a[length] == 2):
        return False
    return True
def Try(i, length):
    for j in tmp:
        a[i] = j
        if(i == length):
            if(check1() and check2(length)):
                for k in range(1, length + 1):
                    print(a[k], end = "")
                print()
        else: Try(i + 1, length)

for i in range(4, n + 1):
    Try(1, i)
