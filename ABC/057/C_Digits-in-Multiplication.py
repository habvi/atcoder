def div_list(x):
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

def F(a, b):
    return max(len(str(a)), len(str(b)))


N = int(input())

ans = float('inf')
for div in div_list(N):
    ans = min(ans, F(div, N // div))
print(ans)
