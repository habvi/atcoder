def digit_sum(x):
    return sum(int(d) for d in str(x))


N = int(input())

digit = [0] * (N + 1)
for i in range(1, N + 1):
    digit[i] = digit_sum(i)

dp = set([N])
ans = set([N])
while dp:
    ndp = set()
    for num in dp:
        for i in range(1, 9 * 6 + 1):
            nxt = num - i
            if nxt in ans:
                continue
            if nxt >= 1:
                if digit[nxt] == i:
                    ndp.add(nxt)
                    ans.add(nxt)
            else:
                break
    dp = ndp
print(len(ans))