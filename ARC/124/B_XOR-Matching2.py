n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = set()
for b in B:
    S.add(A[0] ^ b)

B.sort()
ans = []
for s in S:
    C = []
    for a in A:
        C.append(a ^ s)

    if B == sorted(C):
        ans.append(s)
        
print(len(ans))
print(*sorted(ans))