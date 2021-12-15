n = int(input())
ng = n if n % 2 else n + 1
ans = []
for i in range(1, ng + 1):
    for j in range(i + 1, n + 1):
        if i + j == ng:
            continue
        ans.append((i, j))

print(len(ans))
for a in ans:
    print(*a)