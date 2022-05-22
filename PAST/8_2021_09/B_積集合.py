n, m = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))

A.sort()
for a in A:
    if a in B:
        print(a, end=" ")