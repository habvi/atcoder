def solve(s):
    if len(s) == n:
        print(s)
        return

    for t in "abc":
        solve(s + t)


n = int(input())
solve("")