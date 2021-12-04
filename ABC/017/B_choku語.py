x = input()
for t in ["ch", "o", "k", "u"]:
    x = x.replace(t, "1")
print("YES" if set(x) == {"1"} else "NO")