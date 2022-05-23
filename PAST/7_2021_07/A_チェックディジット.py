S = list(input())
tail = int(S.pop())

total = 0
for i, s in enumerate(S):
    s = int(s)
    if i % 2:
        total += s
    else:
        total += s * 3

print('Yes' if total % 10 == tail else 'No')