S = input()

l = S.find('|')
r = S.rfind('|')
print(l, r, S[:l] + S[r + 1:])
