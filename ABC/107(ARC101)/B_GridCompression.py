h, w = map(int, input().split())
A = [input() for _ in range(h)]

B = []
for a in A:
    if '#' in a:
        B.append(a)

C = []
for b in zip(*B):
    if '#' in b:
        C.append(b)

for ans in zip(*C):
    print(''.join(ans))