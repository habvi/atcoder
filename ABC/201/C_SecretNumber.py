s = input()
ok, ng = set(), set()
for i, ss in enumerate(s):
    if ss == 'o': ok.add(i)
    elif ss == 'x': ng.add(i)

ans = 0
for i in range(10000):
    A = '0' * (4 - len(str(i))) + str(i)
    ok_, ng_ = set(), set()
    for a in A:
        if int(a) in ok:
            ok_.add(int(a))
        if int(a) in ng:
            ng_.add(int(a))

    if len(ng_) == 0 and ok == ok_:
        ans += 1
print(ans)