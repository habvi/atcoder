S = input()

stack = []
alph = [False] * 26
for s in S:
    if s == '(':
        stack.append(s)
        continue
    if s == ')':
        while s:
            t = stack.pop()
            if t == '(':
                break
            i = ord(t) - ord('a')
            alph[i] = False
    else:
        i = ord(s) - ord('a')
        if alph[i]:
            print("No")
            exit()
        else:
            alph[i] = True
        stack.append(s)
print("Yes")