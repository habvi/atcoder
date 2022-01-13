from itertools import product
a = list(map(int, list(input())))

for p in product((1, -1), repeat=3):
    ans = [str(a[0])]
    tot = a[0]
    for i in range(3):
        tot += p[i] * a[i + 1]
        ans.append('+' if p[i] == 1 else '-')
        ans.append(str(a[i + 1]))
    if tot == 7:
        print("".join(ans) + "=7")
        exit()