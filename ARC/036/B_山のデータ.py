n = int(input())
H = [0, *[int(input()) for _ in range(n)]]

ans = 1
down = False
count_ = 0

for i in range(n):
    if H[i] > H[i + 1]:
        down = True

    if down and H[i] < H[i + 1]:
        ans = max(ans, count_)
        down = False
        count_ = 1
    count_ += 1

ans = max(ans, count_)
print(ans)