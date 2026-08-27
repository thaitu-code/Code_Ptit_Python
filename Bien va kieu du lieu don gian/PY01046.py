
def thapHN(n, source, trunggian, dic):
    if(n == 1):
        print(f"{source} -> {dic}")
        return
    thapHN(n - 1, source, dic , trunggian)
    print(f"{source} -> {dic}")
    thapHN(n - 1, trunggian,source , dic)

n = int(input())
thapHN(n, 'A', 'B', 'C')