N = int(input())

S = ['-'] * N
S[N // 2] = '='
if not N % 2:
    S[N // 2 - 1] = '='
print(''.join(S))
