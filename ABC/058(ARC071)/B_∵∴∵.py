A = input()
B = input()

ans = []
for a, b in zip(A, B):
    ans.extend([a, b])

if len(A) > len(B):
    ans.append(A[-1])

print(''.join(ans))