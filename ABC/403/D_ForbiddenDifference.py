N, D = map(int, input().split())
A = list(map(int, input().split()))

M = 10 ** 6
counter = [0] * (M + 1)
for a in A:
    counter[a] += 1

if D == 0:
    print(sum(c - 1 for c in counter if c >= 2))
    exit()

def calc_min_num(nums):
    L = len(nums)
    INF = float('inf')
    # use,rm
    dp = [0] * 2
    for x in nums:
        ndp = [INF] * 2
        ndp[0] = dp[1]
        ndp[1] = min(dp) + x
        dp = ndp
    return min(dp)

ans = 0
for i in range(0, D):
    nums = []
    for j in range(i, M + 1, D):
        nums.append(counter[j])
    ans += calc_min_num(nums)
print(ans)
