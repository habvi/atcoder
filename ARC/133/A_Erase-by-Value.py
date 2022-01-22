n = int(input())
A = list(map(int, input().split()))
erase = -1
for i in range(n - 1):
    if A[i] > A[i + 1]:
        erase = A[i]
        break

if erase == -1:
    erase = A[-1]

ans = []
for a in A:
    if a == erase:
        continue
    ans.append(a)
print(*ans)