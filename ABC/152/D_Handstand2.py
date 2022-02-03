from collections import defaultdict

n = int(input())
d = defaultdict(int)

for i in range(1, n + 1):
    fr = str(i)[0]
    tl = str(i)[-1]
    d[(fr, tl)] += 1

ans = 0
for (ft, tl), c in d.items():
    if (tl, ft) in d:
        ans += c * d[(tl, ft)]
print(ans)



# ans = 0
# for i in range(1, n + 1):
#     if i % 10 == 0:
#         continue
#     ans += d[(str(i)[-1], str(i)[0])]
# print(ans)