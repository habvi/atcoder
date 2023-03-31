N = int(input())
W = set(input().split())

for w in ("and", "not", "that", "the", "you"):
    if w in W:
        print("Yes")
        exit()
print("No")
