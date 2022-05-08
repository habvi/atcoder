n, A, B = map(int, input().split())

for i in range(n):
    for _ in range(A):
        if i % 2:
            ans = ''
            for j in range(n):
                if j % 2:
                    ans += '.' * B
                else:
                    ans += '#' * B
        else:
            ans = ''
            for j in range(n):
                if j % 2:
                    ans += '#' * B
                else:
                    ans += '.' * B
        print(ans)