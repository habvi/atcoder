n = int(input())
S = input()

now = 0
mn = 0
for s in S:
    now += (1 if s == '(' else -1)
    mn = min(mn, now)

T = '(' * -mn + S
res = T.count('(') - T.count(')')

print(T + ')' * res)