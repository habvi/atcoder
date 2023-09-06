N = int(input())

mod = N % 5
if 0 <= mod <= 2:
    ans = N - mod
else:
    ans = N + (5 - mod)
print(ans)