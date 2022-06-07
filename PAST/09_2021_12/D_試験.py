n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

score = []
for i, (a, b) in enumerate(zip(A, B)):
    score.append((a + b, a, i + 1))
score.sort(key=lambda x: (-x[0], -x[1], x[2]))

ans = [i for _, _, i in score]
print(*ans)