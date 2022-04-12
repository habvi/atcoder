import statistics

n = int(input())
A = list(map(int, input().split()))

B = [a - i for i, a in enumerate(A, 1)]
B.sort()

med = int(statistics.median(B))
ans = 0
for b in B:
    ans += abs(b - med)
print(ans)