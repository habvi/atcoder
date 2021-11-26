n = int(input())
s = list('123456')
lis = []
for i in range(30):
    a, b = i % 5, i % 5 + 1
    s[a], s[b] = s[b], s[a]
    lis.append("".join(s))
print(lis[n % 30 - 1])