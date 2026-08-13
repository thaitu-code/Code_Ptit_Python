import sys

n = input().strip()
cnt = 0

if len(n) == 1:
    print(0)
    sys.exit()

while len(n) > 1:
    s = 0
    for char in n:
        s += ord(char) - ord('0')
    
    n = str(s)
    cnt += 1

print(cnt)