S = input()
N = len(S)

ans = 0
for step in range(1, N):
    for start in range(step):
        nums = [S[i] for i in range(start, N, step)]
        for i in range(len(nums) - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] == "ABC":
                ans += 1
print(ans)
