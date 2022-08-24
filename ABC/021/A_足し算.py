N = int(input())

ans = []
for i in range(4):
    if N >> i & 1:
        ans.append(2 ** i)
print(len(ans))
for a in ans:
    print(a)