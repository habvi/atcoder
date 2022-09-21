Y = int(input())

while True:
    if Y % 4 == 2:
        print(Y)
        exit()
    Y += 1


# ---------------
# O(1)
Y = int(input())

mod = Y % 4
a = (6 - mod) % 4
print(Y + a)