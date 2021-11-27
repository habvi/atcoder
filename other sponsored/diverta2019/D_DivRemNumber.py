n = int(input())
s = set()
for i in range(1, int(n ** 0.5) + 1):
    if n % i != 0: continue
    j = n // i
    if j == 1: continue
    j -= 1
    if n // j == n % j:
        s.add(j)
print(sum(s))