N, Q = map(int, input().split())
T = list(map(int, input().split()))

tooth = [1] * N
for t in T:
    t -= 1
    tooth[t] = 1 - tooth[t]
print(sum(tooth))
