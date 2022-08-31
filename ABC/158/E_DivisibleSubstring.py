from collections import Counter

N, P = map(int, input().split())
S = input()
rs = S[::-1]

# P : 2 or 5
if 10 % P == 0:
    ans = 0
    for i, s in enumerate(S, 1):
        if int(s) % P == 0:
            ans += i
    print(ans)
    exit()

ac = [0]
power = 1
for s in rs:
    ac.append((ac[-1] + int(s) * power) % P)
    power *= 10
    power %= P

c = Counter()
ans = 0
for a in ac:
    ans += c[a]
    c[a] += 1
print(ans)