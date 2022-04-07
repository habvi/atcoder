n = int(input())
A = list(map(int, input().split()))

total, minus = 0, 0
mn = float('inf')
for a in A:
    total += abs(a)
    minus += (a < 0)
    mn = min(mn, abs(a))

print(total - mn * 2 if minus % 2 else total)