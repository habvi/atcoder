S = input()
K = int(input())

one = len(S) - len(S.lstrip('1'))

if K <= one:
    ans = '1'
else:
    ans = S[one]
print(ans)