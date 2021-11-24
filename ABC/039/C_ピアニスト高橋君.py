s = input()
ot = ["Do", "", "Re", "", "Mi", "Fa", "", "So", "", "La", "", "Si"]
p = "WBWBWWBWBWBW" * 3
i = p.index(s[:12]) % 12
print(ot[i])