def div_lis(x):
    div_l, div_r = [], []
    for i in range(1, int(x**0.5) + 1):
        if x % i != 0: continue
        div_l.append(i)
        if i != x // i:
            div_r.append(x // i)
    div = div_l + div_r[::-1]
    return div

a, b = map(int, input().split())
da = set(div_lis(a))
db = set(div_lis(b))

def is_prime(num):
    if num == 2:
        return True
    elif num <  3 or num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

ans = 1
for d in da & db:
    if is_prime(d):
        ans += 1
print(ans)