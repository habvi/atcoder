import sys
sys.setrecursionlimit(10 ** 7)

def digit_sum(x):
    return sum(int(d) for d in str(x))

def solve(x):
    if x < 1 or x in ans:
        return

    ans.add(x)
    for i in range(1, 9 * 6 + 1):
        nxt = x - i
        if nxt >= 1:
            if digit[nxt] == i:
                solve(nxt)
        else:
            return


N = int(input())

digit = [0] * (N + 1)
for i in range(1, N + 1):
    digit[i] = digit_sum(i)

ans = set()
solve(N)
print(len(ans))