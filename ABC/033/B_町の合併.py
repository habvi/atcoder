n = int(input())
sp = [tuple(input().split()) for _ in range(n)]
tot = sum(map(lambda x: int(x[1]), sp))
ok = tot // 2 + 1
for s, p in sp:
    if int(p) >= ok:
        print(s)
        exit()
print('atcoder')