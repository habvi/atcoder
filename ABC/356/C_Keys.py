def check(A, x):
    correct = 0
    for a in A:
        if x & (1 << a):
            correct += 1
    return correct >= K


N, M, K = map(int, input().split())
test = [list(input().split()) for _ in range(M)]

ans = 0
for i in range(1 << N):
    for _, *A, R in test:
        A = list(map(lambda x: int(x) - 1, A))
        test_result = check(A, i)
        if (R == "o" and not test_result) or (R == "x" and test_result):
            break
    else:
        ans += 1
print(ans)
