a, b, c = map(int, input().split())

candy = sorted([a, b, c])
print('Yes' if candy[0] + candy[1] == candy[2] else 'No')