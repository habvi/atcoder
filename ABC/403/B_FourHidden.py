def is_ok(S, T):
    for s, t in zip(S, T):
        if s == '?':
            continue
        if s != t:
            return False
    return True


T = input()
U = input()
N, M = len(T), len(U)

for i in range(N - M + 1):
    if is_ok(T[i:i + M], U):
        print("Yes")
        exit()
print("No")
