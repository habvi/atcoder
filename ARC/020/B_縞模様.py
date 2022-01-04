from itertools import combinations
n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = float('inf')
def comp(A, B):
    cnt = 0
    for a, b in zip(A, B):
        if a != b:
            cnt += 1
    return cnt
    
for c1, c2 in combinations(range(1, 11), 2):
    b = []
    for i in range(n):
        if i % 2:
            b.append(c1)
        else:
            b.append(c2)
    ans = min(ans, comp(a, b))
    b = []
    for i in range(n):
        if i % 2 == 0:
            b.append(c1)
        else:
            b.append(c2)
    ans = min(ans, comp(a, b))
print(ans * c)