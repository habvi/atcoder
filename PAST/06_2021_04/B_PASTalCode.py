S = input()

S = S.replace("past", 'x')
S = S.replace("post", 'o')
if (i := S.find('o')) == -1:
    print("none")
else:
    print(i + 1)