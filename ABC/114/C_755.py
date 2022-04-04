from itertools import product

n = int(input())
S = str(n)
m = len(S)

ans = 0
for i in range(3, m + 1):
    for pr in product((3, 5, 7), repeat=i):
        if len(set(pr)) <= 2:
            continue

        x = int(''.join(map(str, pr)))
        ans += (x <= n)

print(ans)