t = int(input())
for i in range(t):
    s1 = input()
    s2 = input()
    s1_sorted = "".join(sorted(s1))
    s2_sorted = "".join(sorted(s2))
    if(s1_sorted == s2_sorted):
        print(f"Test {i + 1}: YES")
    else: print(f"Test {i + 1}: NO")
