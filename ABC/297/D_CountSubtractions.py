def ceil(a, b):
    return (a + b - 1) // b


A, B = map(int, input().split())

ans = 0
while A and B:
    if A < B:
        A, B = B, A
    d = A - B
    ans += ceil(d, B)
    A %= B
print(ans)