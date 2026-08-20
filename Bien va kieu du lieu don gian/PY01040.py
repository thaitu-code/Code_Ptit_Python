cc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate(s):
    cnt = 0
    Lis = list(s)
    for i in range(len(s)):
        cnt += ord(Lis[i]) - ord('A')
    cnt %= 26
    for i in range(len(s)):
        Lis[i] = chr(ord('A') + ((ord(Lis[i]) - ord('A') + cnt) % 26))
    s = "".join(Lis)
    return s
def Merge(s1, s2):
    Lis = list(s1)
    for i in range(len(s1)):
        Lis[i] = chr(ord('A') + ((ord(Lis[i]) - ord('A') + ord(s2[i]) - ord('A')) % 26))
    return "".join(Lis)

t = int(input())
for i in range(t):
    s = input()
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    s1 = rotate(s1)
    s2 = rotate(s2)
    print(Merge(s1, s2))

