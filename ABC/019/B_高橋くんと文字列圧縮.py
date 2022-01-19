from itertools import groupby
s = input()
ans = []
for k, v in groupby(s):
    ans.append(k + str(len(tuple(v))))
print("".join(ans))