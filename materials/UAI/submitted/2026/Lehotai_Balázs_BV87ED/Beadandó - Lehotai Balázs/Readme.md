# Mesterséges  Intelligencia  használata  az  oktatásban
Beadandó  dolgozat | Debrecen, 2026. 04. 28 | Lehotai Balázs, BV87ED

## Feladat: 
A mai oktatásban hasznos segítség lehet a mesterséges intelligencia a fealdatok generálásánál, azonban meg kell tudnunk mondani, hogy egy LLM által generált feladat nehézsége, megfogalmazása és minősége megfelel-e az adott csoport tudásszintjének és az általunk, mint oktató által megfogalmazott követelményeknek.

Mivel ma már bárki futtathat otthon open source LLM modelleket, így dolgozatomban azt vizsgálom, hogy ezek milyen szinten alkalmasak feladatgenerálásra. Referenciaként az OpenAI gpt-5.3 modelljét fogom használni.

A modellek futtatásához használt környet:
Szoftver: Ollama, Windows 11 Pro 25H2
Hardver: Intel Core i9-14000KF, 64 GByte DDR5 RAM, Nvidia RTX 5080 GPU (16 GByte RAM)

## Összehasonlított  modellek:

-  qwen3-coder:30b
-  gemma4:e2b
-  OpenAI gpt-5.3 (referencia)

# 1. Feladatsor generálás prompt alapján
## Prompt:

A 9.-es osztály a programozás  alapjaival  ismerkedik  pythonban. Adj 5 egyszerű  feladatot  példaprogrammal  együtt.

## Eredmények

(a teljes prompt válaszok alul, most csak az 5-5 feladatot emeltem ki, hogy könnyebben összehasonlítható legyen a logika)

#### OpenAI gpt-5.3

**1. Számok  összeadása**

Kérj be két  számot a felhasználótól, és  írd ki az  összegüket.
Példaprogram:

**2. Páros  vagy  páratlan**

Kérj be egy  számot, és  döntsd  el, hogy  páros  vagy  páratlan.

**3. Számok  összege 1-től N-ig**

Kérj be egy  számot (N), és  számold ki az 1-től N-ig  tartó  számok összegét.

**4. Szorzótábla  egy  számhoz**

Kérj be egy számot, és írd ki a szorzótábláját 1-től 10-ig.

**5. Legnagyobb  szám  keresése  listában**

Kérj be 5 számot, tárold  őket listában, majd  írd ki a legnagyobbat.

### Qwen3-coder:30b

**1. Számítások  és  változók**

Kérj be két számot, majd írd ki az összegüket, különbségüket, szorzatukat  és  hányadosukat.

**2. Szöveg  kiírása  és  formázás**

Kérj be egy nevet, majd  írd ki: „Szia [név]!”

**3. Elágazás (if-else)**

Kérj be egy  számot, és  írd ki, hogy  páros  vagy  páratlan.

**4. Ciklus (for)**

Írd ki a számokat 1-től 5-ig.

**5. Lista használata**

Kérj be 3 szót, majd  írd ki őket  egy  listában, és a lista  hosszát is.

### gemma4:e2b

**Feladat 1: A Kiszámítás és a Beviteli Adatok (Input/Output)**
Cél: Megtanuljuk, hogyan fogadjuk be adatokat a felhasználótól, és hogyan megjeleníthetjük a 결과를 (output).

Feladat: Írj egy programot, amely megkérdezi a felhasználót a nevét és az élettartamát, majd megjeleníti őket egy baráti üzenetet.

**Feladat 2: Írj egy programot, amely két számot kér, majd kiszámolja azok összegedet, különbségét, szorzását és osztását.**


**Feladat 3: Feltételezések (If/Else)**

Cél: Megtanuljuk, hogyan használjuk a logikai feltételezéseket (if, elif, else) a programban, hogy a program válaszoljon a feltételekตาม.

Feladat: Írj egy programot, amely megkérdezi a felhasználót egy számot beviteleket, majd ellenőrzi, hogy a szám pozitív-e, negatív-e vagy nullához egyezik-e.

**Feladat 4: Körforgások (For Loop)**

Cél: Megtanuljuk, hogyan használjuk a for körforgásokat, hogy egy adott műveletet ismételjük.

Feladat: Írj egy programot, amely megmutatja a 1-től 10-ig angol számokat.

**Feladat 5: Sorok kezelése (String Manipulation)**

Cél: Megtanuljuk, hogyan manipuláljuk szövegeket (stringeket) a Pythonban.

Feladat: Írj egy programot, amely megkérdezi a felhasználót egy szót beviteleket, majd megjeleníti azt felmásolta (esetleg fordítva).


## Konklúzió

A szöveges válaszokból látható, hogy a modellek hasonló megközelítésű és nehézségű feladatokat adnak. Mindhárom lefedi a kezdő ismereteket, úgy mint: változódeklaráció, input-output, elágazás, ciklusok, aritmetikai műveletek. A gemma modellje bőbeszédűbb, de nagyon magyartalan. A teljes válaszban található python kódokat egy az egyben .py kiterjesztésű fájlokba másoltam, és futtattam őket. Az alábbi táblázat mutatja, hogy az egyes modellek kódjai futnak-e (✅), illetve helyes eredményt adnak (✅✅).

|Futtatható?  | OpenAI gpt-5.3 | qwen3-coder:30b | gemma4:e2b |
|--|--|--|--|
| 1 | ✅✅ | ✅✅ | ⛔ |
| 2 | ✅✅ | ✅✅ | ⛔ |
| 3 | ✅✅ | ✅✅ | ⛔ |
| 4 | ✅✅ | ✅✅ | ✅✅ |
| 5 | ✅✅ | ✅✅ | ⛔ |

A gemma kódja nem python szintaxist használ az értékadásra, illetve nem konzekvens a változónevekkel néhány helyen.

Összegezve megállapíthatjuk, hogy a generált feladatok és a python kódok a gpt-5.3 és a qwen3-coder esetében hasonló minőségűek, a gemma4 viszont jelenleg még alkalmatlan python gyakorlófeladtok generálására.

## Teljes prompt

az [1-prompt-valasz.md] fájlban

# 2. Python kód generálása a felafatleírás alapján

Ebben a részben a gpt-5.2 által készített feladatokat adom a gemma4 illetve quen3-coder modelleknek, és megnézem, hogy a feladat alapján milyen minőségű python kódot generált. A generált python kódok forrásai megtalálhatók a repóban.

## Prompt

Pythonban kódold le a következő öt feladatot:
1. Kérj be két számot a felhasználótól, és írd ki az összegüket.
2. Kérj be egy számot, és döntsd el, hogy páros vagy páratlan.
3. Kérj be egy számot (N), és számold ki az 1-től N-ig tartó számok összegét.
4. Kérj be egy számot, és írd ki a szorzótábláját 1-től 10-ig.
5. Kérj be 5 számot, tárold őket listában, majd írd ki a legnagyobbat.

## Eredmények

Az alábbi táblázat mutatja, hogy az egyes modellek kódjai futnak-e (✅), illetve helyesen implementálják a feladatot (✅✅).

|Futtatható?  | OpenAI gpt-5.3 | qwen3-coder:30b | gemma4:e2b |
|--|--|--|--|
| 1 | ✅✅ | ✅✅ | ✅✅ |
| 2 | ✅✅ | ✅✅ | ✅✅ |
| 3 | ✅✅ | ✅✅ | ✅✅ |
| 4 | ✅✅ | ✅✅ | ✅✅ |
| 5 | ✅✅ | ✅✅ | ✅✅ |

Megállapítható, hogy az előre definiált feladatokat a három llm hasonlóan helyesen oldotta meg. A forráskódokat nézve azonban a gemma4 megoldásain látszik, hogy túlbonyolítottak, feleslegesen bőbeszédűek, és a kivételkezelést is beemelik a kódba (ami kódbiztonság szempontjából helyes, de a diákokat csak összezavarja).

# Végső konklúzió

A qwen3-coder egy dedikáltan kódolásra tanított modell. Jelen teszt alapján ezt biztonsággal lehet használni egyszerűbb programozás feladatok létrehozására. A gpt-5.3 válszaihoz képest nincs jelenős eltérés. A gemma4 egy általános modell, ez látszik a válaszok, illetve a kód minőségén.