

def tong(x):
    sum = 1
    for char in x:
        sum *= int(char)
    return sum

t = int(input())
for i in range(t):
    n = int(input())
    Lis = input().split()
    Lis.sort(key = lambda x : (tong(x), int(x)))
    for i in range(0, len(Lis)):
        print(Lis[i], end = " ")
    print()

