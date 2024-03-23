def accumlate_cost(S, C, is_zero_start):
    cost = [0]
    for i, c in enumerate(C):
        if is_zero_start:
            if i % 2 != int(S[i]):
                cost.append(cost[-1] + c)
            else:
                cost.append(cost[-1])
        else:
            if i % 2 == int(S[i]):
                cost.append(cost[-1] + c)
            else:
                cost.append(cost[-1])
    return cost

def calc_min_cost(s):
    ans = INF
    for i in range(N - 1):
        cost = 0
        if S[i] != s:
            cost += C[i]
        if S[i + 1] != s:
            cost += C[i + 1]

        if i != 0:
            if i % 2 == int(s):
                cost += zero_start_left[i]
            else:
                cost += one_start_left[i]
        if i + 2 < N:
            if i % 2 == int(s):
                cost += one_start_right[i + 2]
            else:
                cost += zero_start_right[i + 2]
        ans = min(ans, cost)
    return ans


N = int(input())
S = input()
C = list(map(int, input().split()))

# -> 0101, 01010
zero_start_left = accumlate_cost(S, C, True)
# 0101, 01010 <-
zero_start_right = accumlate_cost(S[::-1], C[::-1], N % 2 == 1)[::-1]
# -> 1010, 10101
one_start_left = accumlate_cost(S, C, False)
# 1010, 10101 <-
one_start_right = accumlate_cost(S[::-1], C[::-1], N % 2 == 0)[::-1]

INF = float('inf')
# ?00?, ?11?
ans = min(calc_min_cost('0'), calc_min_cost('1'))
print(ans)
