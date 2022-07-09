n, t = map(int, input().split())
A = [int(input()) for _ in range(n)]
A.append(float('inf'))

total = 0
left, right = 0, 0
for a in A:
    if right < a:
        total += (right - left)
        left = a
    right = a + t
print(total)