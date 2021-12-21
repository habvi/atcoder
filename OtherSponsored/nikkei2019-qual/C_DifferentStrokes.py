n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b, a + b))
ab.sort(key=lambda x : x[2], reverse=True)
t, a = 0, 0
for i in range(n):
    if i % 2 == 0:
        t += ab[i][0]
    else:
        a += ab[i][1]
print(t - a)