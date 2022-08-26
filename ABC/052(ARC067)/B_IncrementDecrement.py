N = int(input())
S = input()

now = 0
ans = 0
for s in S:
    if s == 'I':
        now += 1
    else:
        now -= 1
    ans = max(ans, now)
print(ans)