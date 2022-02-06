l, r = map(int, input().split())
MOD = 2019

ans = 2020
mx = l + MOD
for i in range(l, min(r + 1, mx + 1)):
    for j in range(i + 1, min(r + 1, mx + 1)):
        ans = min(ans, i * j % MOD)

print(ans)



# l, r = map(int, input().split())
# MOD = 2019

# ans = 2020
# for i in range(l, r + 1):
#     for j in range(i + 1, r + 1):
#         if ans == 0:
#             print(ans)
#             exit()

#         ans = min(ans, i * j % MOD)
# print(ans)