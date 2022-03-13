from itertools import groupby

n, k = map(int, input().split())
S = input()

T = []
for i, (s, num) in enumerate(groupby(S)):
    if i % 2 and k:
        lr = ('L' if s == 'R' else 'R')
        k -= 1
    else:
        lr = s
    T.append(lr * len(list(num)))

ans = 0
for _, num in groupby(''.join(T)):
    ans += len(list(num)) - 1
print(ans)



# from itertools import groupby

# n, k = map(int, input().split())
# S = input()

# group = 0
# for _, num in groupby(S):
#     group += len(list(num)) - 1

# print(min(n - 1, group + k * 2))