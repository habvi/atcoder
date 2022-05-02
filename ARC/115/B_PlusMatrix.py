n = int(input())
C = [tuple(map(int, input().split())) for _ in range(n)]

B = []
for c in zip(*C):
    B.append(min(c))

A = []
for i in range(n):
    num = set()
    for b, c in zip(B, C[i]):
        num.add(c - b)

    if len(num) != 1:
        print('No')
        exit()

    A.append(num.pop())

print('Yes')
print(*A)
print(*B)