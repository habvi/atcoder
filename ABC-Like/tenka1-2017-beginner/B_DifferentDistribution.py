n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort()
print(sum(ab[-1]))