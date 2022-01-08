n = int(input())
a = []
for i in range(11):
    if i % 2 == 0:
        a.extend(list(range(1, 21)))
    else:
        a.extend(list(range(20, 0, -1)))
print(a[n - 1])