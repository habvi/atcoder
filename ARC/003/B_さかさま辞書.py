n = int(input())
S = []
for _ in range(n):
    s = input()
    S.append((s, s[::-1]))

S.sort(key=lambda x: x[1])

for ans, _ in S:
    print(ans)