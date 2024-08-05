N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
num = B[-2]
print(A.index(num) + 1)
