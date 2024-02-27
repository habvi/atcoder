import string

def ctoi(c):
    return ord(c) - ord('a')


N = int(input())
S = input()
Q = int(input())

A = [[a] for a in string.ascii_lowercase]

for _ in range(Q):
    c, d = input().split()
    for i, a in enumerate(A):
        if a[-1] == c:
            A[i].append(d)

ans = []
for s in S:
    i = ctoi(s)
    ans.append(A[i][-1])
print(''.join(ans))
