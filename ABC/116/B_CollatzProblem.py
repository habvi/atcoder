from collections import defaultdict

s = int(input())

seen = defaultdict(int)
i = 1
while True:
    seen[s] = 1
    if s % 2:
        s = 3 * s + 1
    else:
        s //= 2
    i += 1
    if seen[s]:
        print(i)
        exit()
