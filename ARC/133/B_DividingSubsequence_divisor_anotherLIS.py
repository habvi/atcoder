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

lis = [-1]
ans = 0
for b in B:
    div = div_lis(b)
    div.sort(reverse=True)

    for d in div:
        if lis[-1] < d:
            lis.append(d)
            ans += 1
        else:
            lis[bisect_left(lis, d)] = d

print(ans)