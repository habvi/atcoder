def div_lis(x):
    div = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            div.append(i)
    return div

def length(x):
    return len(str(x))


n = int(input())

ans = float('inf')
for div in div_lis(n):
    ans = min(ans, max(length(div), length(n // div)))

print(ans)