szam1 = float(input("Add meg az első számot: "))
szam2 = float(input("Add meg a második számot: "))
osszeg = szam1 + szam2
print(f"A két szám összege: {osszeg}")


szam = int(input("Add meg a számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")


N = int(input("Add meg a számot (N): "))
osszeg = sum(range(1, N + 1))
print(f"A számok összege 1-től {N}-ig: {osszeg}")


szam = int(input("Add meg a számot: "))
for i in range(1, 11):
    print(f"{szam} x {i} = {szam * i}")


szamok = []
for i in range(5):
    szam = float(input(f"Add meg a {i+1}. számot: "))
    szamok.append(szam)

legnagyobb = max(szamok)
print(f"A legnagyobb szám: {legnagyobb}")