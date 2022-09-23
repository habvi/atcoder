def itoc(i):
    return chr(i + ord('A'))


N, X = map(int, input().split())

S = ""
for i in range(26):
    S += itoc(i) * N
print(S[X - 1])



# ----------------------
# def itoc(i):
#     return chr(i + ord('A'))

# N, X = map(int, input().split())
# X -= 1
# print(itoc(X // N))