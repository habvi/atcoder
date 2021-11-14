n = int(input())
s = list(map(int, input().split()))
cnt = 0
cr = [0] * n
for i in range(1, 1005):
    for j in range(1, 1005):
        a = 4*i*j + 3*i + 3*j
        if a > 1000: continue

        for k in range(n):
            if a == s[k]:
                cr[k] = 1
print(n - sum(cr))


'''
set()あまり速度変わらず

n = int(input())
s = list(map(int, input().split()))
cnt = 0
st = set()
for i in range(1, 1005):
    for j in range(1, 1005):
        a = 4*i*j + 3*i + 3*j
        if a > 1000: continue
        st.add(a)
print(n - sum(1 for i in s if i in st))
'''