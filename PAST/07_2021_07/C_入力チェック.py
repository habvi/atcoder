S = input()
L, R = map(int, input().split())

n = int(S)
if len(S) == len(str(n)) and L <= n <= R:
    print('Yes')
else:
    print('No')