X = input()

if len(set(X)) == 1:
    print('Weak')
    exit()

count_ = 0
for i in range(3):
    if (int(X[i]) + 1) % 10 == int(X[i + 1]):
        count_ += 1

print('Strong' if count_ != 3 else 'Weak')