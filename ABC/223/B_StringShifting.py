S = input()

A = []
for i in range(len(S) + 1):
    A.append(S[i:] + S[:i])
A.sort()

print(A[0], A[-1])