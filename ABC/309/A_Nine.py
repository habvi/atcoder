A, B = map(lambda x: int(x) - 1, input().split())

print("Yes" if A // 3 == B // 3 and abs(A % 3 - B % 3) == 1 else "No")