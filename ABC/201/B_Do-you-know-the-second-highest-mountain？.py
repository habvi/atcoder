n = int(input())
st = [input().split() for _ in range(n)]

st.sort(key=lambda x: int(x[1]))
print(st[-2][0])