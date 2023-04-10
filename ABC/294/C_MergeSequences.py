from bisect import bisect

def calc(A, B):
    ans = []
    for i, a in enumerate(A):
        idx = bisect(B, a)
        ans.append(i + idx + 1)
    print(*ans)

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

calc(A, B)
calc(B, A)