tmp = "ABC"
n = int(input())
for i in range(3, n + 1):
    a = []
    def Try(cnt_a, cnt_b, cnt_c):
        if(len(a) == i):
            if(cnt_a <= cnt_b and cnt_b <= cnt_c and cnt_a >=1):
                print("".join(a))
            return
        for char in tmp:
            if(cnt_a * 3 > i):
                continue
            
            a.append(char)
            if(char == "A"):
                Try(cnt_a + 1, cnt_b, cnt_c)
            elif(char == "B"):
                Try(cnt_a, cnt_b + 1, cnt_c)
            else: Try(cnt_a, cnt_b, cnt_c + 1)
            a.pop()
    Try(0, 0, 0)









