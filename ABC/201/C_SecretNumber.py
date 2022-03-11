def check(x):
    ok = set()
    for i in x:
        if (num := S[int(i)]) == 'x':
            return False

        if num == 'o':
            ok.add(int(i))
    return not (must - ok)


S = input()
must = set()
for i, s in enumerate(S):
    if s == 'o':
        must.add(i)

ans = 0
for num in range(10000):
    if check("%04d" % num):
        ans += 1
print(ans)