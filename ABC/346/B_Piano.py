W, B = map(int, input().split())
S = "wbwbwwbwbwbw" * 25

total = W + B
for i in range(len(S)):
    T = S[i:i + total]
    if T.count('w') == W and T.count('b') == B:
        print("Yes")
        exit()
print("No")
