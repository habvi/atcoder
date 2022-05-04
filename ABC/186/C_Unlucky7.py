n = int(input())

ans = 0
for i in range(1, n + 1):
    ten = str(i).count('7')
    eight = oct(i).count('7')
    ans += (ten + eight == 0)
print(ans)