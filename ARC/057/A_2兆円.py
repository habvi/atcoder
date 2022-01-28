a, k = map(int, input().split())
want = 2 * 10**12
if not k:
    print(want - a)
    exit()

ans = 0
while a < want:
    a += 1 + k * a
    ans += 1
print(ans)