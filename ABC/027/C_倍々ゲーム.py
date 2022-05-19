def move(dir):
    now = 1
    for i in range(bit):
        if i % 2:
            now = now * 2 + (1 - dir)
        else:
            now = now * 2 + dir
        if now > n:
            return i % 2


n = int(input())

bit = n.bit_length()
if bit % 2:
    # right
    win = move(1)
else:
    # left
    win = move(0)

print('Takahashi' if win else 'Aoki')