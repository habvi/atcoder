N = int(input())
S = input()

if N == 2:
    print("Yes" if len(set(S)) == 1 else "No")
    exit()

head = S[0]
tail = S[-1]
print("Yes" if head == 'B' or head + tail == "AA" else "No")