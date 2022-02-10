n = int(input())
H = list(map(int, input().split()))

now = 0
for h in H:
    if h > now:
        now = h
    else:
        break
print(now)