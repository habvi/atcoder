N, R, C = map(int, input().split())
S = input()

smokes = set()
fire_r, fire_c = 0, 0
smokes.add((fire_r, fire_c))
ans = ""
for s in S:
    if s == 'N':
        fire_r += 1
    elif s == 'S':
        fire_r -= 1
    elif s == 'W':
        fire_c += 1
    else:
        fire_c -= 1
    smokes.add((fire_r, fire_c))
    if (fire_r + R, fire_c + C) in smokes:
        ans += '1'
    else:
        ans += '0'
print(ans)
