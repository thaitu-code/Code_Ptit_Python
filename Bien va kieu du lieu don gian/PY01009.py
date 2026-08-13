s = input()
x1, x2 = 0, 0
for char in s:
    if char.islower(): x1+=1
    if char.isupper(): x2+=1
if(x1 >= x2): s = s.lower()
else: s = s.upper()
print(s)