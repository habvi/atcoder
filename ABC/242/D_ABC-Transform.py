def two(s):
    if s == 'A':
        return 'BC'
    elif s == 'B':
        return 'CA'
    else:
        return 'AB'


S = input()

abc = 'ABC'

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    k -= 1

    if t == 0:
        print(S[k])
        continue

    route = [k]
    while k > 0 and t:
        k //= 2
        route.append(k)
        t -= 1

    route = route[::-1]

    if t:
        now = abc[(ord(S[0]) - ord('A') + t - 1) % 3]
        for r in route:
            nxt = two(now)
            now = nxt[r % 2]
    else:
        now = S[route[0]]
        for r in route[1:]:
            nxt = two(now)
            now = nxt[r % 2]
    print(now)