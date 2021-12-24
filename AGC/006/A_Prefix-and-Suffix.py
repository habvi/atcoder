n = int(input())
s = input()
t = input()
for i in range(n):
    if s[i:] == t[:n - i]:
        print(len(s + t[n-i:]))
        exit()
print(n * 2)