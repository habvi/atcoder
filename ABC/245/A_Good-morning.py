a, b, c, d = map(int, input().split())

T = a * 60 + b
A = c * 60 + d + 1

print('Takahashi' if T < A else 'Aoki')