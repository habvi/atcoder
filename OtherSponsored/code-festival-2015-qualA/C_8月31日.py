n, t = map(int, input().split())
ab = []
tot = 0
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, b, a-b))
    tot += a
ab.sort(key=lambda x : x[2], reverse=True)

cnt = 0
for i in range(n):
    if tot <= t:
        print("---", i)
        break
    cnt += 1
    tot -= ab[i][0]
    tot += ab[i][1]
print(cnt if tot <= t else -1)