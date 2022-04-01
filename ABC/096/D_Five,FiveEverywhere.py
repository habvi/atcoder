def primes(max_number):
    pr = list(range(3, max_number + 1, 2))
    ln = len(pr)
    for i, k in enumerate(pr):
        if k:
            if k * k > max_number:
                break
            for j in range(i + k, ln, k):
                pr[j] = 0
    yield 2
    yield from [p for p in pr if p]


n = int(input())

ans = []
for p in primes(55555):
    if p % 5 == 1:
        ans.append(p)

print(*ans[:n])