def longest_common_prefix(S):
    n = len(S)
    lcp = [0] * n
    lcp[0] = n
    i = 1
    j = 0
    while i < n:
        while i + j < n and S[j] == S[i + j]:
            j += 1

        lcp[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i + k < n and k + lcp[k] < j:
            lcp[i + k] = lcp[k]
            k += 1
        i += k
        j -= k
    return lcp


n = int(input())
S = input()

ans = 0
for i in range(n - 1):
    lcp = longest_common_prefix(S[i:])

    for j, num in enumerate(lcp):
        ans = max(ans, min(j, num))
print(ans)