def div_lis(x):
    div_l, div_r = [], []
    i = 1
    while i * i <= x:
        if x % i == 0:
            div_l.append(i)
            if i != x // i:
                div_r.append(x // i)
        i += 1
    div = div_l + div_r[::-1]
    return div


n = int(input())

ans = set(div for div in div_lis(n - 1))
ans.remove(1)

for i in div_lis(n)[1:]:
    x = n
    while x % i == 0:
        x //= i
    if x % i == 1:
        ans.add(i)
print(len(ans))