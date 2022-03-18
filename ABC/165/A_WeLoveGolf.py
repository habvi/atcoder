K = int(input())
a, b = map(int, input().split())

mul = b // K - (a - 1) // K
print('OK' if mul >= 1 else 'NG')