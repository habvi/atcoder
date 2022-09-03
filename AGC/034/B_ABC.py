S = input()

S = S.replace("BC", "X")
ans = 0
for s in S.split('C'):
    for t in s.split('B'):
        a = 0
        for u in t:
            if u == 'A':
                a += 1
            else:
                ans += a
print(ans)