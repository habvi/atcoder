N = int(input())
A = list(map(int, input().split()))

for i in range(2, N):
    if A[i] == A[i - 1] == A[i - 2]:
        print("Yes")
        exit()
print("No")
