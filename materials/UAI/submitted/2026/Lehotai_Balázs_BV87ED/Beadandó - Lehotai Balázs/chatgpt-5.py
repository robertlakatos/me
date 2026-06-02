szamok = []

for i in range(5):
    szam = int(input("Adj meg egy számot: "))
    szamok.append(szam)

legnagyobb = szamok[0]

for szam in szamok:
    if szam > legnagyobb:
        legnagyobb = szam

print("A legnagyobb szám:", legnagyobb)