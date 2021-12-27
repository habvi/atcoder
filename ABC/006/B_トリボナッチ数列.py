from collections import deque
n = int(input())
MOD = 10007
d = deque([0, 0, 1], 3)
if n <= 2:
    print(d[n - 1])
    exit()

for _ in range(n - 3):
    d.append(sum(d) % MOD)
print(d[-1])