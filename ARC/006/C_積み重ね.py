n = int(input())

box = []
for _ in range(n):
    w = int(input())

    for i, b in enumerate(box):
        if w <= b:
            box[i] = w
            break
    else:
        box.append(w)

print(len(box))