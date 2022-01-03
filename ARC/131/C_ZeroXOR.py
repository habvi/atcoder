n = int(input())
A = list(map(int, input().split()))
if n % 2 == 1:
    print('Win')
    exit()

xor = 0
for a in A:
    xor ^= a
if xor in A:
    print('Win')
else:
    print('Lose')