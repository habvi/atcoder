s = input()
t = input()
a = "atcoder"
n = len(s)
for i in range(n):
    if s[i] == t[i]:
        continue
    if s[i] != '@' and t[i] != '@':
        print('You will lose')
        exit()
    if s[i] in a or t[i] in a:
        continue
    else:
        print('You will lose')
        exit()
print('You can win')