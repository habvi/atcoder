N = input()

digit = len(N)
cut = max(0, digit - 3)
x = 10 ** cut
print(int(N) // x * x)