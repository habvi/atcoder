S1, S2 = input().split()

SICK = "sick"
if S1 == S2 == SICK:
    print(1)
elif S1 == SICK:
    print(2)
elif S2 == SICK:
    print(3)
else:
    print(4)
