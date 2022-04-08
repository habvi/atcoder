n = int(input())
L = list(map(int, input().split()))

ans = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            cand = [L[i], L[j], L[k]]
            a, b, c = sorted(cand)
            if a == b or b == c or c == a:
                continue
            if a + b > c:
                ans.append(cand)
print(len(ans))