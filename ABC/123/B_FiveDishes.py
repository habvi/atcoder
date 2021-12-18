total = 0
mn = []
for _ in range(5):
    a = int(input())
    r = a % 10
    if r == 0:
        total += a
    else:
        total += a - r + 10
        mn.append(r - 10)
print(total + (min(mn) if mn else 0))