n = int(input())
s = [int(input()) for _ in range(5)]
mn = min(s)
print((n + mn - 1) // mn + 4)