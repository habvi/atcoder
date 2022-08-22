N = int(input())

s = set()
for a in range(2, int(N ** 0.5) + 1):
    b = 2
    while a ** b <= N:
        s.add(a ** b)
        b += 1
print(N - len(s))