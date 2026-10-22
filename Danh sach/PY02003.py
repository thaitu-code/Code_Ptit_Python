import sys


def haming():
    Limit = 10**18
    ham = []
    val2 = 1
    while(val2 <= Limit):
        val3 = val2
        while(val3 <= Limit):
            val5 = val3
            while(val5 <= Limit):
                ham.append(val5)
                val5 *= 5
            val3 *= 3
        val2 *= 2
    ham.sort()
    return ham
ham_tmp = haming()
input_data = sys.stdin.read().split()
if(input_data):
    t = int(input_data[0])
    out = []
    for i in range(1, len(input_data)):
        n = int(input_data[i])
        ok = 0
        l = 0
        r = len(ham_tmp) - 1
        while(l <= r):
            m = (l + r) // 2
            if(int(ham_tmp[m]) == n):
                ok = m + 1
                break
            elif(int(ham_tmp[m]) < n):
                l = m + 1
            else:
                r = m - 1
        if(ok > 0):
            out.append(str(ok))
        else:
            out.append("Not in sequence")
    sys.stdout.write("\n".join(out) + "\n")