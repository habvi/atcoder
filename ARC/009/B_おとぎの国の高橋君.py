b = list(input().split())
n = int(input())
d = {v : i for i, v in enumerate(b)}
a = [input() for _ in range(n)]

a.sort(key=lambda x: (len(x),) + tuple(d[i] for i in x))
for ans in a:
    print(ans)