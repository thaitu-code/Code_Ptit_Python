
s1 = input().lower()
s2 = input().lower()
Lis1 = s1.split()
Lis2 = s2.split()
Set1 = set()
Set2 = set()
Set = set()
for num in Lis1:
    Set.add(num)
    Set1.add(num)
for num in Lis2:
    Set.add(num)
    Set2.add(num)
Lis = list(Set)

Lis.sort()
Lis3 = []
for char in Lis:
    print(char, end = " ")
print()
for char1 in Set1:
    ok = 1
    for char2 in Set2:
        if(char1 == char2):
            ok = 0
            break
    if(ok == 0):
        Lis3.append(char1)
Lis3.sort()
for i in Lis3:
    print(i, end = " ")

