n = int(input())
a = list(map(int, input().split()))
dic = {}
for char in a:
    if(char not in dic):
        dic[char] = 1
        # print(char)
for i in range(1, 30001):
    if(i not in dic):
        print(i)
        break