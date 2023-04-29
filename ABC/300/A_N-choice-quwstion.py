N, A, B = map(int, input().split())
C = list(map(int, input().split()))

total = A + B
print(C.index(total) + 1)