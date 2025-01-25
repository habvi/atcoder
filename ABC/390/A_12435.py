A = list(map(int, input().split()))

sorted = sorted(A)
for i in range(4):
    A[i], A[i + 1] = A[i + 1], A[i]
    if A == sorted:
        print("Yes")
        exit()
    A[i], A[i + 1] = A[i + 1], A[i]
print("No")
