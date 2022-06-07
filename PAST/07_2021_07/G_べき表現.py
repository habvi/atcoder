n = int(input())

ans = []
x = n
k = 1
mod = 0
while x != 0:
    mod = x % 3
    if mod:
        ans.append(k * (1 if mod == 1 else -1))
    k *= 3

    if mod:
        x = (x + (-1 if mod == 1 else 1)) // 3
    else:
        x //= 3

print(len(ans))
print(*ans)