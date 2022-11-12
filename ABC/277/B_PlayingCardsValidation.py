N = int(input())
first = "HDCS"
second = "A23456789TJQK"

seen = set()
for _ in range(N):
    S = input()
    if (S in seen) or (S[0] not in first) or (S[1] not in second):
        print("No")
        exit()
    seen.add(S)
print("Yes")