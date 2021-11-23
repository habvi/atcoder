# print(654231) or

me = [i for i in range(1, 7)]
st = max(me)
ans = [st]
now = st

ng = set()
while len(ng) != 6:
    ng.add(now)
    ng.add(7 - now)
    for i in range(6, 0, -1):
        if i in ng:
            continue
        ans.append(i)
        if 7 - now not in ans:
            ng.remove(7 - now)
        now = i
        break
print(''.join(map(str, ans)))