def match(pattern, num_str):
    for i in range(2):
        if pattern[i] != '?' and pattern[i] != num_str[i]:
            return False
    return True

t = int(input())
for i in range(t):
    parts = input().split()
    if(parts[1] == "*" or parts[1] == "/"):
        print("WRONG PROBLEM!")
        continue
    x1, x2, x3 = parts[0], parts[2], parts[4]
    ok  = 0
    for i in range(10, 100):
            if(ok == 1):
                break
            tmp = str(i)
            if(not match(x1, tmp)):
                continue
            for j in range(10, 100):
                if(ok == 1): break
                tmp1 = str(j)
                if(not match(x2, tmp1)):
                    continue
                for k in range(10, 100):
                    tmp2 = str(k)
                    if(ok == 1): break
                    if(not match(x3, tmp2)):
                        continue
                    if(parts[1] == '?'):
                        if(int(tmp) - int(tmp1) == int(tmp2)):
                            print(f'{tmp} - {tmp1} = {tmp2}')
                            ok = 1
                        elif(int(tmp) + int(tmp1) == int(tmp2)):
                            print(f'{tmp} + {tmp1} = {tmp2}')
                            ok = 1
                    elif(parts[1] == '-'):
                        if(int(tmp) - int(tmp1) == int(tmp2)):
                            print(f'{tmp} - {tmp1} = {tmp2}')
                            ok = 1
                    else:
                        if(int(tmp) + int(tmp1) == int(tmp2)):
                            print(f'{tmp} + {tmp1} = {tmp2}')
                            ok = 1
    if(ok == 0):
        print("WRONG PROBLEM!")
                    


