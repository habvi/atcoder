na, nb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sa = set(a)
sb = set(b)

print(len(sa & sb) / len(sa | sb))