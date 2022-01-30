from collections import deque

n = int(input())
S = input()

d = deque([n])
for i, s in enumerate(S[::-1]):
    if s == 'L':
        d.append(n - i - 1)
    else:
        d.appendleft(n - i - 1)
print(*d)