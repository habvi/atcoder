n = int(input())
A = list(map(int, input().split()))

A.sort()
mx = A.pop()
half = mx / 2

B = [(abs(half - a), a) for a in A]
B.sort()
print(mx, B[0][1])



# from bisect import bisect

# n = int(input())
# A = list(map(int, input().split()))

# A.sort()
# mx = A.pop()
# half = mx / 2
# bi = bisect(A, half)

# if bi == len(A):
#     print(mx, A[bi - 1])
#     exit()

# if abs(half - A[bi - 1]) < abs(half - A[bi]):
#     print(mx, A[bi - 1])
# else:
#     print(mx, A[bi])