N, X = map(int, input().split())
A = list(map(int, input().split()))

st = set()
for a in A:
    st.add(a)
    if (X + a in st) or (a - X in st):
        print("Yes")
        exit()
print("No")
