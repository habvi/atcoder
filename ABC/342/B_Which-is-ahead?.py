N = int(input())
P = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    ai = P.index(a)
    bi = P.index(b)
    if ai < bi:
        print(a)
    else:
        print(b)
