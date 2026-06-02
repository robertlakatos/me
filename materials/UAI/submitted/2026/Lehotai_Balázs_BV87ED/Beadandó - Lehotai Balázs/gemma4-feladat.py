# Python kód, amely 5 feladatot végrehajt
import math # Ez a modull a 3. feladathoz (opcionális, de hasznos lehet)

print("=========================================")
print("    FELADAT 1: Két szám összege")
print("=========================================")

# 1. Kérj be két számot a felhasználótól, és írd ki az összegüket.
try:
    num1 = float(input("Kérje be a pertama számot: "))
    num2 = float(input("Kérje be a második számot: "))
    
    sum_result = num1 + num2
    print(f"\nAz két szám összege: {sum_result}")

except ValueError:
    print("\nHibás beviteli adat! Kérjük, ne adja meg szöveget számként.")


print("\n=========================================")
print("    FELADAT 2: Páros vagy Páratlan")
print("=========================================")

# 2. Kérj be egy számot, és döntsd el, hogy páros vagy páratlan.
try:
    number = int(input("Kérje be egy egész számot: "))
    
    # Ha a szám 2-rel osztva maradékban 0-ban van, páros.
    if number % 2 == 0:
        print(f"\nAz {number} szám páros.")
    else:
        print(f"\nAz {number} szám páratlan.")

except ValueError:
    print("\nHibás beviteli adat! Kérjük, adja meg egy egész számot.")


print("\n=========================================")
print("    FELADAT 3: Számok összege (1-től N-ig)")
print("=========================================")

# 3. Kérj be egy számot (N), és számold ki az 1-től N-ig tartó számok összegét.
try:
    N = int(input("Kérje be a számot (N), amivel szeretné számolni: "))
    
    if N >= 1:
        # Számoljuk ki a 1-től N-ig tartó számok összegét
        total_sum = 0
        for i in range(1, N + 1):
            total_sum += i
        
        # Alternativban, ha ismerjük a formát (aritmetikai sorozat):
        # total_sum = N * (N + 1) // 2
        
        print(f"\nAz 1-től {N}-ig tartó számok összege: {total_sum}")
    else:
        print("\nA szám pozitívnek kell lennie.")

except ValueError:
    print("\nHibás beviteli adat! Kérjük, adja meg egy egész számot.")


print("\n=========================================")
print("    FELADAT 4: Szorzótáblázat")
print("=========================================")

# 4. Kérj be egy számot, és írd ki a szorzótábláját 1-től 10-ig.
try:
    multiplier = int(input("Kérje be a számot, amelynek szorzótáblázatot szeretné írni (1-től 10-ig): "))
    
    print(f"\n--- {multiplier} szorzótáblázata ---")
    for i in range(1, 11):
        result = multiplier * i
        # Formázjuk a kiírt szöveget, hogy látható legyen
        print(f"{multiplier} x {i} = {result}")

except ValueError:
    print("\nHibás beviteli adat! Kérjük, adja meg egy egész számot.")


print("\n=========================================")
print("    FELADAT 5: Legnagyobb szám")
print("=========================================")

# 5. Kérj be 5 számot, tárold őket listában, majd írd ki a legnagyobbat.
numbers = []
print("Kérje be 5 számot:")

for i in range(5):
    while True:
        try:
            num = float(input(f"Szám {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Hibás beviteli adat! Kérjük, adja meg egy számot.")

# Használjuk a Python-t built-in max() funkciót a legnagyobb szám megtalálásához
if numbers:
    largest_number = max(numbers)
    print(f"\nA bevitelt számok listája: {numbers}")
    print(f"A legnagyobbat a listában: {largest_number}")
else:
    print("\nNincs adat a legnagyobb szám meghatározásához.")
