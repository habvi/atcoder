n, m = map(int, input().split())
A = [int(input()) for _ in range(m)]

A = A[::-1]
A.extend(range(1, n + 1))

done = set()
for a in A:
    if a not in done:
        print(a)
        done.add(a)