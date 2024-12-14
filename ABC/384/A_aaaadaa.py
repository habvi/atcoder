N, c1, c2 = input().split()
S = input()

ans = [c2 if s != c1 else s for s in S]
print("".join(ans))
