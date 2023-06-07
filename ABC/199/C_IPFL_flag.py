N = int(input())
S = list(input())
Q = int(input())
swap = 0
N2 = 2 * N
for _ in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        A, B = A - 1, B - 1
        if swap:
            A, B = (A + N) % N2, (B + N) % N2
        S[A], S[B] = S[B], S[A]
    else:
        swap = 1 - swap
print(''.join(S[N:] + S[:N]) if swap else ''.join(S))