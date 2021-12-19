n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]
done = set()
for b in a[::-1]:
    if b not in done:
        print(b)
        done.add(b)

for i in range(1, n + 1):
    if i not in done:
        print(i)
        done.add(i)