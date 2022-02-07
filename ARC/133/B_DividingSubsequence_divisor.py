from bisect import bisect_left
def div_lis(x):
    div = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            div.append(ai[i])
            if i != x // i:
                div.append(ai[x // i])
        i += 1
    return div


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ai = {a : i for i, a in enumerate(A)}

lis = [float('inf')] * (n + 1)
for b in B:
    div = div_lis(b)
    div.sort(reverse=True)

    for d in div:
        bi = bisect_left(lis, d)
        lis[bi] = d

ans = bisect_left(lis, n + 1)
print(ans)