# 1 20 20 20 20 ...
# 20 1 20 20 20 ...
# 20 20 1 20 20 ...
#       :
# 20回試して得点をscoreに入れてsort

n = 20
score = [827, 791, 793, 811, 797, 
         807, 813, 805, 803, 801,
         823, 815, 825, 799, 809,
         795, 817, 821, 829, 819]

result = []
for s, i in zip(score, range(n)):
    result.append((s, i))
result.sort()

ans = [None] * n
for num, (_, i) in enumerate(result):
    ans[i] = n - num

print(*ans)