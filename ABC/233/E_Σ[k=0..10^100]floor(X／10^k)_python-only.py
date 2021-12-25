from itertools import accumulate
x = list(input())
x = list(map(int, x))

ac = list(accumulate(x))
ans = ""
k = 0
for i in range(len(x) - 1, -1, -1):
    k += ac[i]
    ans += str(k % 10)
    k //= 10
print(str(k) + ans[::-1] if k else ans[::-1])