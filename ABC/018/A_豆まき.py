A = [int(input()) for _ in range(3)]

d = {}
for i, a in enumerate(sorted(A, reverse=True), 1):
    d[a] = i

for a in A:
    print(d[a])