n = int(input())

ans = 0
for _ in range(n):
    a, b = map(int, input().split())
    d = b - a

    nums = [0] * 6
    for i, yen in enumerate((500, 100, 50, 10, 5, 1)):
        num = d // yen
        nums[i] = num
        d -= num * yen
        if not d:
            break

    ans += nums[2] + nums[4]
print(ans)