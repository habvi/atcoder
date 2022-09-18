N = int(input())
A = list(map(int, input().split()))

total = sum(A)
ans = float('inf')
left = 0
for a in A:
    left += a
    right = total - left
    ans = min(ans, abs(right - left))
print(ans)