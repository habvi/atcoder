A, B = map(int, input().split())

ans = 0
for i in range(3):
    if A >> i & 1 or B >> i & 1:
        ans += 2 ** i
print(ans)



# ------------------
# A, B = map(int, input().split())
# print(A | B)