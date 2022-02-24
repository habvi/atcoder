a, b, t = map(int, input().split())

span = b - a
ans = b
while ans < t:
    ans += span

print(ans)