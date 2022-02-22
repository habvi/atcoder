def sum_digit(x):
    return sum(int(c) for c in str(x))


n = int(input())

len_ = len(str(n))
maxi = 9 * len_
start = max(0, n - maxi)

ans = []
for x in range(start, n + 1):
    if x + sum_digit(x) == n:
        ans.append(x)

print(len(ans))
for num in sorted(ans):
    print(num)