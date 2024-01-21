N = int(input())
A = list(map(int, input().split()))

s = set(A)
for i in range(1, N + 1):
    if i not in s:
        tail = i
        break

ans = []
ans.append(tail)
i = tail - 1
while True:
    ni = A[i]
    if ni == -1:
        break
    ans.append(ni)
    i = ni - 1
print(*ans[::-1])