n = int(input())
S = input() + 'C'

a, b = 0, 0
ans = []
for s in S:
    if s == 'C':
        ans.append('A' * (a + b//2))
        if b % 2:
            ans.append('B')
        a, b, = 0, 0
        ans.append(s)
        continue

    if s == 'A':
        a += 1
    else:
        b += 1

print(''.join(ans[:-1]))