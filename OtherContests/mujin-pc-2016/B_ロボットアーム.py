from math import pi

def circle_s(r):
    return r * r * pi


oa, ab, bc = map(int, input().split())

sumr = oa + ab + bc
maxr = max(oa, ab, bc)
min2r = sum(sorted([oa, ab, bc])[:2])

if maxr > min2r:
    print(circle_s(sumr) - circle_s(maxr - min2r))
else:
    print(circle_s(sumr))