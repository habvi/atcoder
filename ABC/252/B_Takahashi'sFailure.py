n, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx = max(A)
idx = [i for i, a in enumerate(A, 1) if a == mx]

for b in B:
    if b in idx:
        print('Yes')
        exit()
print('No')