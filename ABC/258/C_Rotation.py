N, Q = map(int, input().split())
S = input()

i = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        i = (i - x) % N
    else:
        print(S[(x + i - 1) % N])