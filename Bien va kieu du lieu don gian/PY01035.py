def chuyen(t):
    ans = 0
    while(len(t) > 0):
        tmp = t[-3:]
        t = t[:-3]
        tmp_reverse = tmp[::-1]
        tmp1 = 0
        for i in range(0, len(tmp)):
            tmp1 += pow(2, i) * int(tmp_reverse[i])
        ans = ans * 10 + tmp1
    ans_reverse = 0
    while(ans > 0):
        ans_reverse = ans_reverse * 10 + ans % 10
        ans //=10
    return ans_reverse

t = input()
print(chuyen(t))