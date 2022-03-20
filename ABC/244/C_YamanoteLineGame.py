n = int(input())
m = 2*n + 1

s = set()
while True:
    for i in range(1, m + 1):
        if i not in s:
            T = i
            break
    print(T, flush=True)
    s.add(T)

    if len(s) == m:
        break

    num = int(input())
    s.add(num)