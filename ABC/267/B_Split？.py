S = input()

B = [[6], [3], [1, 7], [0, 4], [2, 8], [5], [9]]
if S[0] == '1':
    print("No")
    exit()

for i in range(7):
    for j in range(i + 2, 7):
        if any(S[k] == '1' for k in B[i]) and any(S[k] == '1' for k in B[j]):
            for k in range(i + 1, j):
                if all(S[l] == '0' for l in B[k]):
                    print("Yes")
                    exit()
print("No")
