N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    for i, a in enumerate(A):
        if a:
            print(i + 1, end=" ")
    print()
