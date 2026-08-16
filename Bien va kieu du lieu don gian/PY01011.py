def check1(s):
    # s.split()
    for i in range(len(s)):
        if((int(s[i])) % 2 != 0):
            return False
    return True
def check2(s):
    return len(s) % 2 == 0
def check3(s):
    s1 = s[::-1]
    return s1 == s
t = int(input())
for i in range(t):
    s = int(input())
    for i in range(22, s, 2):
        if(check3(str(i)) and check2(str(i)) and check1(str(i))):
            print(i,end= " ")
    print(end = "\n")
    


