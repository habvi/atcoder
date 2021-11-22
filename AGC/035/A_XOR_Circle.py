from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
ls = len(c)
def No():
    print('No')
    exit()

if ls == 1:
    print('Yes' if list(c.keys())[0] == 0 else 'No')
    exit()

if n % 3 != 0: No()

if ls == 2:
    k, _ = c.most_common(1)[0]
    if k == 0: No()
    a, b = c.values()
    if a > b: a, b = b, a
    if a * 2 == b:
        print('Yes')
    else:
        print('No')
    exit()

if ls == 3:
    ok = 0
    k1, k2, k3 = c.keys()
    if k1 ^ k2 == k3:
        ok +=1
    v = list(c.values())
    if v[0] == v[1] == v[2]:
        ok += 1
    if ok == 2:
        print('Yes')
        exit()
print('No')