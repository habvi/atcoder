from collections import defaultdict

n, m = map(int, input().split())
A = list(map(int, input().split()))

idx = defaultdict(list)
for i, a in enumerate(A):
    idx[a].append(i)

for i in range(n + 1):
    num = [-1, *idx[i], n]

    for j in range(len(num) - 1):
        if num[j + 1] - num[j] > m:
            print(i)
            exit()