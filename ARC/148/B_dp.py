N = int(input())
S = input()

ans = S[:]
i = 0
for s in S:
    if s == "d":
        i += 1
    else:
        break
head = S[:i]
S = S[i:]

for i in range(len(S) + 1):
    mid = ['d' if s == 'p' else 'p' for s in S[:i][::-1]]
    T = head + ''.join(mid) + S[i:]
    if ans > T:
        ans = T
print(ans)
