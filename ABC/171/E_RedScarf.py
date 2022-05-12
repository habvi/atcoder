from functools import reduce
from operator import xor

n = int(input())
A = list(map(int, input().split()))

ac = reduce(xor, A)

ans = [ac ^ a for a in A]
print(*ans)