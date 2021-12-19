from itertools import permutations
n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]
cd = [tuple(map(int, input().split())) for _ in range(m)]
cd.sort()
for per in permutations([i + 1 for i in range(n)]):
    after = []
    for a, b in ab:
        after.append(tuple(sorted([per[a-1], per[b-1]])))
    after.sort()
    if cd == after:
        print('Yes')
        exit()
print('No')