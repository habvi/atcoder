def calc_total(is_zero_start, S):
    cost = [0]
    for i, c in enumerate(C):
        if is_zero_start:
            if i % 2 == 0 and S[i] == '1':
                cost.append(cost[-1] + c)
            elif i % 2 and S[i] == '0':
                cost.append(cost[-1] + c)
            else:
                cost.append(cost[-1])
        else:
            if i % 2 == 0 and S[i] == '0':
                cost.append(cost[-1] + c)
            elif i % 2 and S[i] == '1':
                cost.append(cost[-1] + c)
            else:
                cost.append(cost[-1])
    return cost

def calc_total_rev(is_zero_start, S):
    cost = [0]
    for i, c in enumerate(C[::-1]):
        s2 = '0' if len(S) % 2 else '1'
        s1 = '1' if len(S) % 2 else '0'
        if is_zero_start:
            if i % 2 == 0 and S[i] == s1:
                cost.append(cost[-1] + c)
            elif i % 2 and S[i] == s2:
                cost.append(cost[-1] + c)
            else:
                cost.append(cost[-1])
        else:
            if i % 2 == 0 and S[i] == s2:
                cost.append(cost[-1] + c)
            elif i % 2 and S[i] == s1:
                cost.append(cost[-1] + c)
            else:
                cost.append(cost[-1])
    return cost

def calc_cost_zero():
    ans = INF
    for i in range(N - 1):
        cost = 0
        if S[i] != '0':
            cost += C[i]
        if S[i + 1] != '0':
            cost += C[i + 1]

        if i != 0:
            if i % 2:
                cost += one_start_left[i]
            else:
                cost += zero_start_left[i]
        if i + 2 < N:
            if i % 2:
                cost += zero_start_right[i + 2]
            else:
                cost += one_start_right[i + 2]
        ans = min(ans, cost)
    return ans

def calc_cost_one():
    ans = INF
    for i in range(N - 1):
        cost = 0
        if S[i] != '1':
            cost += C[i]
        if S[i + 1] != '1':
            cost += C[i + 1]

        if i != 0:
            if i % 2:
                cost += zero_start_left[i]
            else:
                cost += one_start_left[i]
        if i + 2 < N:
            if i % 2:
                cost += one_start_right[i + 2]
            else:
                cost += zero_start_right[i + 2]
        ans = min(ans, cost)
    return ans


N = int(input())
S = input()
C = list(map(int, input().split()))

# 0101
zero_start_left = calc_total(True, S)
zero_start_right = calc_total_rev(True, S[::-1])[::-1]
# 1010
one_start_left = calc_total(False, S)
one_start_right = calc_total_rev(False, S[::-1])[::-1]

INF = float('inf')
ans = min(calc_cost_zero(), calc_cost_one())
print(ans)
