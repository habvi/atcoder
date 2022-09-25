from itertools import groupby

n, k = map(int, input().split())
S = input()

T = []
for i, (s, v) in enumerate(groupby(S)):
    v = len(list(v))
    if i % 2 and k:
        s = ('L' if s == 'R' else 'R')
        k -= 1
    T.append(s * v)

ans = 0
for _, v in groupby(''.join(T)):
    ans += len(list(v)) - 1
print(ans)


# from itertools import groupby

# n, k = map(int, input().split())
# S = input()

# group = 0
# for _, num in groupby(S):
#     group += len(list(num)) - 1

# print(min(n - 1, group + k * 2))