K = int(input())
a = bin(K)[2:]
ans = []
for b in a:
    if b == "1":
        ans.append("2")
    else:
        ans.append("0")
print("".join(ans))