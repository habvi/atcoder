n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a0 = A[0]
cand = set(a0 ^ b for b in B)

ans = []
B.sort()
for num in cand:
    c = [a ^ num for a in A]
    if sorted(c) == B:
        ans.append(num)

print(len(ans))
print(*sorted(ans))