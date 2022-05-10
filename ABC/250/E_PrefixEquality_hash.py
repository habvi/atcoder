# hash
import random

def gen_hash(A):
    hash = []
    used = set()
    pre = 0
    for a in A:
        if a not in used:
            pre ^= new[a]
            used.add(a)
        hash.append(pre)
    return hash


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = set(ab for ab in [*A, *B])
rdm = random.sample(range(1, 1 << 61), len(s))
new = {x : nx for x, nx in zip(s, rdm)}

hash_a = gen_hash(A)
hash_b = gen_hash(B)

Q = int(input())
for _ in range(Q):
    x, y = map(lambda x: int(x) - 1, input().split())

    print('Yes' if hash_a[x] == hash_b[y] else 'No')