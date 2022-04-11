from collections import Counter

def ceil(a, b):
    return (a + b - 1) // b


n, m = map(int, input().split())
name = input()
kit = input()

cn = Counter(name)
ck = Counter(kit)

ans = 0
for k, v in cn.items():
    if not ck[k]:
        print(-1)
        exit()
    ans = max(ans, ceil(v, ck[k]))

print(ans)