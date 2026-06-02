
#### OpenAI gpt-5.3

**1. Számok  összeadása**

Feladat:  
Kérj be két  számot a felhasználótól, és  írd ki az  összegüket.
Példaprogram:

    a = int(input("Add meg az  első  számot: "))  
    b = int(input("Add meg a második  számot: ")) 
    
    osszeg = a + b  
    print("Az összeg:", osszeg)

**2. Páros  vagy  páratlan**

Feladat:  
Kérj be egy  számot, és  döntsd  el, hogy  páros  vagy  páratlan.

Példaprogram:

    szam = int(input("Adj meg egy számot: "))  
      
    if szam % 2 == 0:  
        print("A szám  páros.")  
    else:  
        print("A szám  páratlan.")

**3. Számok  összege 1-től N-ig**

Feladat:  
Kérj be egy  számot (N), és  számold ki az 1-től N-ig  tartó  számok összegét.

Példaprogram:

    n = int(input("Adj meg egy  számot: "))  
    osszeg = 0  
        
    for i in range(1, n + 1):  
        osszeg += i  
        
    print("Az összeg:", osszeg)

**4. Szorzótábla  egy  számhoz**

Feladat:  
Kérj be egy számot, és írd ki a szorzótábláját 1-től 10-ig.

Példaprogram:

    szam = int(input("Adj meg egy  számot: "))  
      
    for i in range(1, 11):  
        print(szam, "*", i, "=", szam * i)

**5. Legnagyobb  szám  keresése  listában**

Feladat:  
Kérj be 5 számot, tárold  őket listában, majd  írd ki a legnagyobbat.

Példaprogram:

    szamok = []  
  
    for i in range(5):  
        szam = int(input("Adj meg egy  számot: "))  
        szamok.append(szam)  
      
    legnagyobb = szamok[0]  
      
    for szam in szamok:  
        if szam > legnagyobb:  
        legnagyobb = szam  
      
    print("A legnagyobb  szám:", legnagyobb)

#### Qwen3-coder:30b

**1. Számítások  és  változók**

Feladat: Kérj be két számot, majd írd ki az összegüket, különbségüket, szorzatukat  és  hányadosukat.

    a = int(input("Add meg az  első  számot: "))  
    b = int(input("Add meg a második számot: "))  
    
    print("Összeg:", a + b)  
    print("Különbség:", a - b)  
    print("Szorzat:", a * b)  
    print("Hányados:", a / b)  

**2. Szöveg  kiírása  és  formázás**

Feladat: Kérj be egy nevet, majd  írd ki: „Szia [név]!”

    nev =  input("Add meg a neved: ")  
    print("Szia", nev, "!")  

**3. Elágazás (if-else)**

Feladat: Kérj be egy  számot, és  írd ki, hogy  páros  vagy  páratlan.

    szam = int(input("Adj meg egy  számot: "))  
    
    if szam %  2  ==  0:  
    print("A szám  páros.")  
    else:  
    print("A szám  páratlan.")  

**4. Ciklus (for)**

Feladat: Írd ki a számokat 1-től 5-ig.

    for i in  range(1, 6):  
    print(i)  

**5. Lista használata**

Feladat: Kérj be 3 szót, majd  írd ki őket  egy  listában, és a lista  hosszát is.

    szavak = []  
    for i in  range(3):  
    szo =  input(f"Add meg a {i+1}. szót: ")  
    szavak.append(szo)  
    
    print("A szavak  listája:", szavak)  
    print("A lista  hossza:", len(szavak))

#### gemma4:e2b

**Feladat 1: A Kiszámítás és a Beviteli Adatok (Input/Output)**
Cél: Megtanuljuk, hogyan fogadjuk be adatokat a felhasználótól, és hogyan megjeleníthetjük a 결과를 (output).

Feladat: Írj egy programot, amely megkérdezi a felhasználót a nevét és az élettartamát, majd megjeleníti őket egy baráti üzenetet.

Példaprogram:

    # 1. Beviteli adatok bevitele
    nev <- input("Kérem, írja be a nevét: ")
    elettartam <- input("Kérem, írja be az élettartamát (évben): ")

    #2. Ausztrix (String) kombinációk használata
    print("Szia,", nev + "! Nagyon örülök, hogy", str(elettartam) + " éves vagy!")

Magyarázat:

A input() függvény használjuk az adott sorban a felhasználó beviteli adatait (ez mindig stringként történik).
A print() függvény megjeleníti a szöveget a képernyőn.
A str() függvényt használjuk, hogy az egész számot szöveggé alakítsuk, hogy a + operátor megfelelően működjön.
Feladat 2: Alapvető Matematikai Kiszámítás
Cél: Megtanuljuk, hogyan használjuk a matematikai operátorokat (pl. +, -, *, /) a programokban.

**Feladat 2: Írj egy programot, amely két számot kér, majd kiszámolja azok összegedet, különbségét, szorzását és osztását.**

Példaprogram:

    # 1. Számok bevitele
    szam_a <- int(input("Kérem, írja be a first számot: "))
    szam_b <- int(input("Kérem, írja be a second számot: "))

    # 2. Kiszámítások
    sum <- sam_a + sam_b
    diff <- sam_a - sam_b
    product <- sam_a * sam_b
    quotient <- sam_a / sam_b

    # 3. Eredmények megjelenítése
    print("\n--- Kiszámítások ---")
    print("Összeadás (Sum):", sum)
    print("Különbség (Difference):", diff)
    print("Szorzás (Product):", product)
    print("Osztás (Quotient):", quotient)

Magyarázat:

A int() függvényt használjuk a beviteli adatokat számokká (integerekre) alakítva.
A +, -, *, / operátorok azonnal végrehajtják a matematikai műveleteket.

**Feladat 3: Feltételezések (If/Else)**

Cél: Megtanuljuk, hogyan használjuk a logikai feltételezéseket (if, elif, else) a programban, hogy a program válaszoljon a feltételekตาม.

Feladat: Írj egy programot, amely megkérdezi a felhasználót egy számot beviteleket, majd ellenőrzi, hogy a szám pozitív-e, negatív-e vagy nullához egyezik-e.

Példaprogram:

    szam <- int(input("Kérem, írja be egy számot: "))

    if sam > 0:
        print("A szám pozitív.")
    elif sam < 0:
        print("A szám negatív.")
    else:
        print("A szám nullához egyezik.")

Magyarázat:

A if megkezdő a feltétel. Ha a feltétel igaz (True), akkor a kódot a if blokkon belül futtatja.
A elif (else if) lehetővé teszi több feltétel egy sorban ellenőrzését.
A else blokk a legvége, ami fut körben, ha az korábbi feltételek sem igazak.

**Feladat 4: Körforgások (For Loop)**

Cél: Megtanuljuk, hogyan használjuk a for körforgásokat, hogy egy adott műveletet ismételjük.

Feladat: Írj egy programot, amely megmutatja a 1-től 10-ig angol számokat.

Példaprogram:

    print("1-től 10-ig számoljuk:")

    # A for körforgás használata
    # range(1, 11) jelenti, hogy a körforgás 1-től kezdődjön és 11-től korlátozzon (nem fogja belefoglalni a 10-et)
    for i in range(1, 11):
        print(i)

Magyarázat:

A for körforgás használjuk, amikor egy adott kódsorokat (iterációkat) ismételjük.
A range(start, stop) függvényt használjuk, hogy meghatározzuk, mely számok között futtasson a körforgás.

**Feladat 5: Sorok kezelése (String Manipulation)**

Cél: Megtanuljuk, hogyan manipuláljuk szövegeket (stringeket) a Pythonban.

Feladat: Írj egy programot, amely megkérdezi a felhasználót egy szót beviteleket, majd megjeleníti azt felmásolta (esetleg fordítva).

Példaprogram:

    szov <- input("Kérem, írja be egy szót: ")

    # 1. Szó felmásolása (String szorozatok felhasználásával)
    felmasolat <- szov + " felmásolt"
    print("A szót felmásolta: ", szov)
    print("A felmásolás eredménye: ", felmasolat)

    # 2. Szó fordítása (A Python-ban a szorozatokhoz van built-in funkció)
    fordit <- szov[::-1]
    print("A szót fordítva: ", fordit)

Magyarázat:

A szorozatok (stringek) a szöveg tárolására szolgálnak.
A + operátor használatával szorozatokat lehet összekapcsolni.
A [::-1] sintaxis a Pythonban egy nagyon gyors módszer a szorozatok fordítására. A [start:stop:step] formátum használjuk, ahol a -1 lépés a fordított irányt jelenti.
