A, B, C = map(int, input().split())

if (not C and A > B) or (C and A >= B):
    print("Takahashi")
else:
    print("Aoki")