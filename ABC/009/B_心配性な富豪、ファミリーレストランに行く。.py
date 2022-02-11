from collections import Counter

n = int(input())
A = [int(input()) for _ in range(n)]
print(sorted(Counter(A).keys())[-2])