ans = []
for w in input():
    if w not in 'aiueo':
        ans.append(w)
print(''.join(ans))