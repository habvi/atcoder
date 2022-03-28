n = int(input())
S = input()
K = int(input())

t = S[K - 1]
ans = ['*' if s != t else s for s in S]
print(''.join(ans))