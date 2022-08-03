n = int(input())
A = list(map(int, input().split()))

total, minus = 0, 0
mn = float('inf')
for a in A:
    total += abs(a)
    minus += (a < 0)
    mn = min(mn, abs(a))

print(total - mn * 2 if minus % 2 else total)



# -------------------------------
N = int(input())
A = list(map(int, input().split()))

minus = 0
for a in A:
    minus += (a < 0)

B = list(map(abs, A))
if minus % 2:
    print(sum(B) - min(B) * 2)
else:
    print(sum(B))