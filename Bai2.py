import sys


def solve(n, mod, s):
    m = len(s)

    if mod == 1 or n < m:
        return 0

    pi = [0] * m

    for i in range(1, m):
        j = pi[i - 1]

        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]

        if s[i] == s[j]:
            j += 1

        pi[i] = j

    overlap = [0] * (m + 1)
    overlap[0] = 1

    border = pi[-1]

    while border > 0:
        overlap[m - border] = 1
        border = pi[border - 1]

    rec = [
        26 * overlap[i - 1] - overlap[i]
        for i in range(1, m + 1)
    ]
    rec[-1] -= 1

    terms = [
        (i + 1, coefficient)
        for i, coefficient in enumerate(rec)
        if coefficient != 0
    ]

    def multiply(a, b):
        temp = [0] * (2 * m - 1)

        for i, x in enumerate(a):
            if x == 0:
                continue

            for j, y in enumerate(b):
                temp[i + j] += x * y

        for degree in range(2 * m - 2, m - 1, -1):
            value = temp[degree] % mod

            if value == 0:
                continue

            for shift, coefficient in terms:
                temp[degree - shift] += value * coefficient

        return [temp[i] % mod for i in range(m)]

    result = [0] * m
    result[0] = 1

    base = [0] * m

    if m == 1:
        base[0] = rec[0] % mod
    else:
        base[1] = 1

    exponent = n

    while exponent > 0:
        if exponent & 1:
            result = multiply(result, base)

        exponent >>= 1

        if exponent > 0:
            base = multiply(base, base)

    without_s = 0
    initial = 1

    for coefficient in result:
        without_s = (
            without_s + coefficient * initial
        ) % mod

        initial = initial * 26 % mod

    return (pow(26, n, mod) - without_s) % mod


def main():
    data = sys.stdin.buffer.read().split()

    t = int(data[0])
    pos = 1
    answers = []

    for _ in range(t):
        n = int(data[pos])
        mod = int(data[pos + 1])
        s = data[pos + 2].decode()
        pos += 3

        answers.append(str(solve(n, mod, s)))

    sys.stdout.write("\n".join(answers))


main()