x, y = map(int, input().split())
ans = 0
for i in range(105):
    if x >= y:
        print(ans)
        exit()
    x += 10
    ans += 1


# x, y = map(int, input().split())
# print(max(0, (y - x + 9) // 10))