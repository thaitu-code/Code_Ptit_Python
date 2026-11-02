import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    out = []
    INF = float('inf')
    for _ in range(T):
        n = int(data[idx]); idx += 1
        t = sorted(int(x) for x in data[idx:idx + n])
        idx += n

        m = 2 * n
        dp = [[INF] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i][j - 1],
                               dp[i - 1][j - 1] + abs(t[i - 1] - j))
        out.append(str(dp[n][m]))

    print("\n".join(out))

main()