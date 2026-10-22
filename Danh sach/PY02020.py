n = int(input())
a = list(map(float, input().split()))
Max = 0
Min = 10
for char in a:
    Max = max(Max, char)
    Min = min(Min, char)
ans = 0
cnt = 0
for char in a:
    if(char != Max and char != Min):
        ans += char
        cnt += 1
ans /= cnt
print(f"{ans:.2f}")