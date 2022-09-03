S = input()

B = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]
if S[0] == '1':
    print("No")
    exit()

for i in range(7):
    for j in range(i + 1, 7):
        if j - i <= 1:
            continue
        if any(S[b] == '1' for b in B[i]) and any(S[b] == '1' for b in B[j]):
            for k in range(i + 1, j):
                for b in B[k]:
                    if S[b] == '1':
                        break
                else:
                    print("Yes")
                    exit()
print("No")
