from collections import Counter, defaultdict
def nC2(n):
    return n*(n - 1) // 2

n = int(input())
A = list(map(int, input().split()))
c = Counter(A)

case = defaultdict(int)
case2 = defaultdict(int)
tot = 0
for k, v in c.items():
    tot += nC2(v)
    case[k] = nC2(v)
    case2[k] = nC2(v - 1)

for a in A:
    print(tot - case[a] + case2[a])