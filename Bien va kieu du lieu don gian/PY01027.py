
def check(n):
    i = 0
    while(i < len(n)):
        if(i + 2 <= len(n) - 1 and n[i:i + 3] == "688"):
            i += 2
        elif(i + 1 <= len(n) - 1 and n[i:i + 2] == "68"):
            i+=1
        elif(n[i] == "6"):
            i+=1
            continue
        else:
            return False
        i+=1
    return True

n = input()
n.split()
if(check(n)):
    print("YES")
else: print("NO")
