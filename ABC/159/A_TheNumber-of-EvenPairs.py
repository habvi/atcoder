def nC2(x):
    return x * (x - 1) // 2

n, m = map(int, input().split())
ans = nC2(n) + nC2(m)
print(ans)