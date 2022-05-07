T = int(input())

for _ in range(T):
    l, r = map(int, input().split())
    n, m = len(str(l)), len(str(r))

    if n == m:
        print(r - l + 1)
    else:
        mid = 10 ** (m - 1)
        dr = r - mid + 1

        if dr >= mid:
            print(dr)
        else:
            print(dr + mid - max(l, r % mid + 1, r // 10 + 1))