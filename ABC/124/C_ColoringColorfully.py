S = input()

odd = 0
even = 0
k = '1'
for i, s in enumerate(S):
    if i % 2:
        odd += (s == k)
        even += (s != k)
    else:
        odd += (s != k)
        even += (s == k)

print(min(odd, even))