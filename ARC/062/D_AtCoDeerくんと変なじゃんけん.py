S = input()

ans = 0
for i, s in enumerate(S):
    if i % 2 == 0 and s == 'p':
        ans -= 1
    elif i % 2 and s == 'g':
        ans += 1

print(ans)