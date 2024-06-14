def calc(A):
    pyra = [0]
    for a in A:
        pyra.append(min(a, pyra[-1] + 1))
    return pyra


N = int(input())
A = list(map(int, input().split()))

left = calc(A)
right = calc(A[::-1])[::-1]
ans = 1
for i in range(N):
    ans = max(ans, min(left[i + 1], right[i]))
print(ans)
