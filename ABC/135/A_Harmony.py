a, b = map(int, input().split())

d = a + b
print(d // 2 if d % 2 == 0 else 'IMPOSSIBLE')