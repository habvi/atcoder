cnt = [0] * 4
for _ in range(3):
    a, b = map(lambda x: int(x) - 1, input().split())
    cnt[a] += 1
    cnt[b] += 1
cnt.sort()
print('YES' if cnt == [1, 1, 2, 2] else 'NO')