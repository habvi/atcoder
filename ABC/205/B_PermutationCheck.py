n = int(input())
a = sorted(map(int, input().split()))
print('Yes' if a == list(range(1, n + 1)) else 'No')