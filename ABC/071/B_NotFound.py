s = input()
st = set(s)
for i in range(ord('a'), ord('z') + 1):
    if chr(i) not in st:
        print(chr(i))
        exit()
print('None')