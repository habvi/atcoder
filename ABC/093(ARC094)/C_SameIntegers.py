a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c])

if (b - a) % 2 == 0:
    x, y, z = a, b, c
elif (c - b) % 2 == 0:
    x, y, z = b, c, a
else:
    x, y, z = a, c, b

ans = (y - x) // 2

if y < z:
    ans += z - y
else:
    ans += ((y - z + 1)//2 + 1 if (y - z) % 2 else (y - z)//2)
print(ans)



# a, b, c = map(int, input().split())

# total = sum([a, b, c])
# mx = max(a, b, c)
# diff = mx * 3 - total

# if diff % 2 == 0:
#     ans = diff // 2
# else:
#     ans = ((mx + 1)*3 - total) // 2
# print(ans)