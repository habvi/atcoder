H, W = map(int, input().split())

for _ in range(H):
    S = list(input())
    for i in range(W - 1):
        if S[i] == S[i + 1] == 'T':
            S[i] = 'P'
            S[i + 1] = 'C'
    print(''.join(S))