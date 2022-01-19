t = ['H', '2B', '3B', 'HR']
s = [input() for _ in range(4)]
print('Yes' if sorted(t) == sorted(s) else 'No')