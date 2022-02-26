n, k = map(int, input().split())
A = list(map(int, input().split()))

x = 0
a = A[x]

s = set()
idx = []
num = []

for _ in range(n):
    if x in s:
        break
    s.add(x)
    idx.append(x)

    a = A[x]
    x += a
    x %= n
    num.append(a)

front = idx.index(x)

if k <= front:
    print(sum(num[:k]))
    exit()

total = sum(num[:front])
num = num[front:]
k -= front

ln = len(num)
total += k // ln * sum(num) + sum(num[:k % ln])
print(total)