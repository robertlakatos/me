# 1. Két szám összege
a = float(input("Adj meg egy számot: "))
b = float(input("Adj meg még egy számot: "))
print("Összeg:", a + b)


# 2. Páros vagy páratlan
n = int(input("\nAdj meg egy egész számot: "))
if n % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")


# 3. 1-től N-ig összeg
N = int(input("\nAdj meg egy számot (N): "))
osszeg = sum(range(1, N + 1))
print("Az összeg:", osszeg)


# 4. Szorzótábla 1-től 10-ig
szam = int(input("\nAdj meg egy számot: "))
print("Szorzótábla:")
for i in range(1, 11):
    print(f"{szam} x {i} = {szam * i}")


# 5. 5 szám közül a legnagyobb
lista = []
print("\nAdj meg 5 számot:")
for i in range(5):
    szam = float(input(f"{i+1}. szám: "))
    lista.append(szam)

print("A legnagyobb szám:", max(lista))