def stoi(s):
    return ord(s) - ord('a')

def itos(i):
    return chr(i + ord('a'))


S = input()

if S in ('a', 'z' * 20):
    print('NO')
    exit()

S = list(S)
n = len(S)
if n == 1:
    print(itos(stoi(S[0]) - 1) + 'a')
    exit()

if len(set(S)) == 1:
    if S[0] == 'a':
        S.pop()
        S[-1] = 'b'
    elif S[0] == 'z':
        S.pop()
        S.append('ya')
    else:
        S[0] = itos(stoi(S[0]) + 1)
        S[1] = itos(stoi(S[1]) - 1)
    print(''.join(S))
else:
    for i in range(n):
        for j in range(i + 1, n):
            if S[i] != S[j]:
                S[i], S[j] = S[j], S[i]
                print(''.join(S))
                exit()