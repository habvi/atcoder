n = int(input())
T = list(map(int, input().split()))

now = 0
for t in T:
    num = 1 << t
    mask = (1 << t + 1) - 1

    right = now & mask
    left = bin(now)[2:][:-(t + 1)]
    if not left:
        left = '0'

    if num <= right:
        left = int(left, 2) + 1
    else:
        left = int(left, 2)
    now = (left << t + 1) | num

print(now)