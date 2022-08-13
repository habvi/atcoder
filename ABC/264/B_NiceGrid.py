R, C = map(lambda x: int(x) - 1, input().split())

if R >= 8:
    R = 14 - R

ans = "white"
if R % 2 == 0:
    if R <= C <= 14 - R:
        ans = "black"
    else:
        if C % 2 == 0:
            ans = "black"
else:
    if not (R <= C <= 14 - R) and C % 2 == 0:
        ans = "black"
print(ans)