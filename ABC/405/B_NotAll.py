N, M = map(int, input().split())
A = list(map(int, input().split()))

s = set()
for i, a in enumerate(A):
    s.add(a)
    if len(s) == M:
        print(N - i)
        exit()
print(0)
