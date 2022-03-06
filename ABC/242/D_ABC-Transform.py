def stoi(s):
    return ord(s) - ord('A')


S = input()
A = 'ABC'

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    k -= 1

    if t == 0:
        print(S[k])
        continue

    route = [k]
    while k and t:
        k //= 2
        route.append(k)
        t -= 1

    start = A[(stoi(S[route[-1]]) + t) % 3]

    route.pop()
    route = route[::-1]

    idx = stoi(start)
    for r in route:
        if r % 2:
            idx += 2
        else:
            idx += 1
        idx %= 3

    print(A[idx])