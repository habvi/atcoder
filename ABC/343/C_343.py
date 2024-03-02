N = int(input())

ans = 1
for i in range(10 ** 6 + 1):
    x = i ** 3
    if x <= N:
        s = list(str(x))
        if s == s[::-1]:
            ans = x
print(ans)
