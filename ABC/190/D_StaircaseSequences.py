def div_lis(x):
    div_l, div_r = [], []
    for i in range(1, int(x**0.5) + 1):
        if x % i != 0:
            continue
        div_l.append(i)
        if i != x // i:
            div_r.append(x // i)
    div = div_l + div_r[::-1]
    return div


n = int(input())

ans = 0
n2 = n * 2
for d in div_lis(n2):
    if d % 2 != n2 // d % 2:
        ans += 1
print(ans)



# ---------------------
'''
n * (a + l) // 2 == N
'''
# N *= 2
# ans = 0
# for x in div_list(N):
#     y = N // x
#     ans += (y - (x - 1)) % 2 == 0
# print(ans)
