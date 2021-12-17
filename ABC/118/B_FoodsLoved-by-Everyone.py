n, m = map(int, input().split())
ans = set(list(map(int, input().split()))[1:])
for _ in range(n - 1):
    k = set(list(map(int, input().split()))[1:])
    ans &= k
print(len(ans))