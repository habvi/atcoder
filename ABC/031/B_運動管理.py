l, h = map(int, input().split())
n = int(input())
for _ in range(n):
    a = int(input())
    if h < a:
        print(-1)
    elif a < l:
        print(l - a)
    else:
        print(0)