s = [input() for _ in range(2)]
b1 = s[0][0] + s[1][1]
w1 = s[0][1] + s[1][0]
b2 = s[0][1] + s[1][0]
w2 = s[0][0] + s[1][1]
if (b1 == "##" and w1 == "..") or (b2 == "##" and w2 == ".."):
    print('No')
else:
    print('Yes')