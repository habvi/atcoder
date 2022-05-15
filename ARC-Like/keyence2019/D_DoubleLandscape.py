from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 10**9 + 7

row_s = set(A)
col_s = set(B)
if len(row_s) != n or len(col_s) != m:
    print(0)
    exit()

c = Counter(A)
for b in B:
    c[b] += 1

ans = 1
row, col = 0, 0
for i, num in enumerate(reversed(range(1, n * m + 1))):
    if i == 0 and c[num] != 2:
        print(0)
        exit()

    if c[num] == 2:
        row += 1
        col += 1
        continue

    if c[num]:
        if num in row_s:
            row += 1
            ans *= col
        if num in col_s:
            col += 1
            ans *= row
        ans %= MOD
        continue

    ans *= row * col - i
    ans %= MOD
print(ans)