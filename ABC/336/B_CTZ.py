N = int(input())

b = bin(N)
ans = 0
for c in b[::-1]:
    if c == "0":
        ans += 1
    else:
        break
print(ans)
