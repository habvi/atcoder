n = int(input())
S = input()
st = []
cnt = 0
for s in S:
    st.append(s)
    if "".join(st[-3:]) == 'fox':
        for _ in range(3):
            st.pop()
        cnt += 1
print(n - cnt * 3)