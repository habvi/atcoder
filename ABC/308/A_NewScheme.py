def c1(S):
    for s in S:
        if not (100 <= s <= 675):
            return False
    return True

def c2(S):
    for s in S:
        if s % 25:
            return False
    return True

def c3(S):
    size = len(S)
    for i in range(size - 1):
        if not S[i] <= S[i + 1]:
            return False
    return True


S = list(map(int, input().split()))

print("Yes" if c1(S) and c2(S) and c3(S) else "No")
