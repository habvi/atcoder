def stoi(s):
    return ord(s) - ord('A')


n = int(input())

num = [0] * 6
ans = [None] * 6
for i in range(1, n + 1):
    p, v = input().split()
    pi = stoi(p)
    if v == 'AC':
        if not num[pi]:
            ans[pi] = i
            num[pi] = 1
print(*ans)