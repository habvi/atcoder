from collections import defaultdict

N, T = map(int, input().split())

num = defaultdict(int)
num[0] = N
score = [0] * N
for _ in range(T):
    a, b = map(int, input().split())
    i = a - 1
    pre = score[i]
    num[pre] -= 1
    if not num[pre]:
        del num[pre]
    score[i] += b
    num[score[i]] += 1
    print(len(num))
