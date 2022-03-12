n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = set(B)

ans1 = 0
ans2 = 0
for a, b in zip(A, B):
    if a == b:
        ans1 += 1
    else:
        if a in s:
            ans2 += 1
print(ans1, ans2)