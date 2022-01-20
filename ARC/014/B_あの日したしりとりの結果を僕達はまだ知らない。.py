n = int(input())
S = [input() for _ in range(n)]

last = S[0][0]
used = set()
for i, s in enumerate(S):
    if s in used or s[0] != last:
        win = 1 if i % 2 else 0
        print('WIN' if win else 'LOSE')
        exit()
    used.add(s)
    last = s[-1]
print('DRAW')