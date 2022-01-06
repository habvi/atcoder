n = int(input())
s = set()
for i in range(1, int(n ** 0.5) + 1):
    if n % i != 0:
        continue
    j = n // i
    for k in (i, j):
        k -= 1
        if k == 0:
            continue
        if n // k == n % k:
            s.add(k)
print(sum(s))