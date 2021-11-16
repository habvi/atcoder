n = int(input())
A = list(map(int, input().split()))
two, four, odd = 0, 0, 0
for a in A:
    if a % 4 == 0:
        four += 1
    elif a % 2 == 0:
        two += 1
    else:
        odd += 1

ans = True
if odd:
    if two:
        if four != odd:
            ans = False
    else:
        if not four or odd > four + 1:
            ans = False
print('Yes' if ans else 'No')