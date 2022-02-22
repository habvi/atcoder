n = int(input())

odd = [int(input()) % 2 for _ in range(n)]
print('first' if sum(odd) > 0 else 'second')