---
title: "Introduction to AI and Decision Making"
collection: teaching
type: "M.Sc course"
permalink: materials/AIPD/labor/IV-pe-hu
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2026-09-16
location: "Debrecen, Hungary"
---

# Prompt Engineering

# Gyakorlati Prompt Engineering a Geminivel

Ez a laborgyakorlat a nagy nyelvi modellekkel (LLM) való hatékony kommunikációt, vagyis a prompt engineering (prompt-tervezés) technikáit mutatja be. A cél, hogy a mesterséges intelligenciát ne csupán egy keresőmotorként, hanem egy programozható kognitív asszisztensként tudd használni.

## 1. In-context learning (Kontextuson belüli tanulás)

A nyelvi modellek egyik legfontosabb sajátossága az **in-context learning**. Ez azt jelenti, hogy a modell képes új mintákat, szabályokat vagy feladatokat megtanulni és alkalmazni *kizárólag a promptban átadott információk alapján*, anélkül, hogy a belső (szerkezeti) súlyait újra kellene tanítani. Ha adsz neki egy új keretrendszert a beszélgetésen belül, a modell azonnal alkalmazkodik hozzá.

> **Demonstrációs példa:**
> *Felhasználó:* "A mi belső céges zsargonunkban a 'Kék Pingvin' egy olyan ügyfelet jelent, aki sokat kérdez, de sosem vásárol. A 'Piros Leopárd' pedig azt, aki azonnal fizet kérdések nélkül. Ezt figyelembe véve, elemezd az alábbi értékesítői jelentést: 'Ma bejött egy srác, egy órát faggatott a garanciáról, majd kiment. Utána jött egy hölgy, aki rámutatott a legdrágább gépre és a bankkártyájával fizetett.'"
> *Modell válasza:* "Az első ügyfél egy tipikus Kék Pingvin volt, míg a második egy egyértelmű Piros Leopárd."

## 2. Zero-shot learning (Példa nélküli tanulás)

A **Zero-shot learning** során a modelltől úgy kérünk megoldást egy feladatra, hogy semmilyen előzetes példát nem adunk meg neki a promptban. Ilyenkor a modell kizárólag a betanítása során elsajátított hatalmas, általános tudásbázisára támaszkodik a feladat értelmezésekor.

> **Példa:** "Osztályozd az alábbi vásárlói véleményt (Pozitív, Negatív, Semleges): *A szoftver felülete átlátható, de az adatexport funkció nagyon lassú.*"

* **Hallgatói feladat a Geminiben:**
Adj a Gemininek egy Zero-shot promptot, amelyben arra kéred, hogy írjon egy 3 soros, professzionális visszautasító e-mailt egy álláspályázónak. Ne adj meg neki sablont vagy példát, hagyd, hogy magától generálja le a formátumot! Futasd akár többször újabb és újabb chat ablak indításával és figyeld meg a különbségeket.

## 3. Few-shot learning (Kevés példás tanulás)

Ha a Zero-shot nem hoz elég pontos eredményt, vagy egy nagyon specifikus kimeneti formátumra van szükségünk, **Few-shot learninget** alkalmazunk. Ilyenkor a promptban adunk 2-3 (vagy több) konkrét mintát a bemenet-kimenet párosításra, így a modell megtanulja az általunk elvárt logikát és formátumot.

> **Példa:**
> Alakítsd át a nyers termékneveket a webshopunk kategória-rendszerébe!
> Nyers: iPhone 14 Pro -> Kategória: Okostelefonok
> Nyers: LG 55 colos 4K -> Kategória: Televíziók
> Nyers: Bosch robotgép -> Kategória: Konyhai gépek
> Nyers: Samsung Galaxy S23 -> Kategória: ?

* **Hallgatói feladat a Geminiben:**
Van egy rendszertelen címlistád (pl. "Budapest kossuth Lajos utca 12 1053", "Szeged, 6720 Kárász u. kilenc"). Készíts egy Few-shot promptot 3 példával, ami megtanítja a Geminit arra, hogy a beírt nyers címeket pontosan egy ilyen JSON formátumba alakítsa át: `{"Irányítószám": "...", "Város": "...", "Utca_házszám": "..."}`. Teszteld le egy új címmel!

## 4. System prompt (Rendszer prompt)

A **System prompt** a nyelvi modell "személyiségét", viselkedési szabályait és korlátait határozza meg a beszélgetés legelején. Ez az a háttér-instrukció, ami alapján az AI értelmezi a későbbi, sima felhasználói kérdéseket. (A Geminiben ezt úgy szimulálhatod, ha az első üzenetedben szigorúan definiálod a szerepét azaz a perszónát.)

**Fontos:** A nagy rendszerek saját system prompt-al dolgoznak amit perszónával finomíthatsz de felül nem írhatod azt.

> **Példa:**
> "Ettől a perctől kezdve te egy szigorú, adatalapú kockázatelemző vagy. Bármilyen üzleti ötletet írok le, a válaszodban mindig a legrosszabb forgatókönyvre (worst-case scenario) és a pénzügyi kockázatokra kell fókuszálnod. Soha ne legyél túlzottan optimista. A válaszaid legyenek rövidek és tárgyilagosak."

## 5. Rhetorical Prompt Engineering (Retorikai promptolás)

A retorikai promptolás az emberi kommunikáció technikáinak (perszónák, érvelési struktúrák, célközönség meghatározása) alkalmazása. Nem csak azt mondjuk meg a gépnek, hogy *mit* csináljon, hanem azt is, hogy *kinek*, *milyen stílusban* és *milyen szándékkal*. Ezzel finomhangoljuk a válasz árnyalatait.

> **Példák:**
> * "Magyarázd el a neurális hálózatok működését egy 10 éves gyereknek az ő nyelvén."
> * "Érvelj amellett, hogy a felhőalapú adattárolás veszélyes, úgy, mintha te lennél a '90-es évek egyik vezető kiberbiztonsági szakértője, aki gyanakszik az új technológiákra."
> 
> 

* **Hallgatói feladatok a Geminiben:**
1. Kérd meg a Geminit, hogy magyarázza el a korreláció és kauzalitás (ok-okozat) közötti különbséget egy szkeptikus cégvezetőnek, aki egy rossz statisztika miatt épp most akar kirúgni egy egész osztályt.
2. Kérj tőle egy rövid Python kódmagyarázatot, de add ki az utasítást úgy: "Magyarázd el ezt a kódsort úgy, mintha Gordon Ramsay lennél, és a kódom tele lenne amatőr hibákkal."

## 6. Meta promptolás

A **Meta promptolás** az, amikor a nyelvi modellt arra használjuk fel, hogy *saját maga* hozzon létre, értékeljen, vagy javítson promptokat. Nem a végső feladatot oldatjuk meg vele, hanem a gépiesítjük a jobb kérdésfeltevést.

* **Hallgatói feladatok a Geminiben:**
1. Írd be ezt a Gemininek: *"Szeretnék egy olyan gépi tanulási modellt építeni Pythonban, ami megjósolja az ügyfelek elvándorlását. Írj nekem 3 olyan tökéletes, részletes promptot, amit ha később visszatáplálok neked, a lehető legjobb segítséget és kódvázlatot fogod tudni adni nekem a munkához."*
2. Írj egy nagyon rossz, hiányos promptot a Gemininek (pl. *"csinálj táblázatot adatokkal"*). Rögtön utána kérd meg: *"Kritizáld meg az előző promptomat! Mondd el, mi hiányzik belőle, és írd át úgy, hogy egy profi adatelemző promptja legyen!"*

## 7. Extra promptolási technikák

* **Chain-of-Thought (Gondolatmenet, Lépésről-lépésre):** Arra kényszerítjük a modellt, hogy fejtse ki a logikai lépéseit, mielőtt megadja a végső választ. Ez drasztikusan csökkenti a hallucinációt matematikai vagy logikai feladatoknál.
* **Feladat:** Kérdezz meg egy összetett logikai fejtörőt (pl. "Ha 5 gép 5 perc alatt 5 terméket gyárt, mennyi idő alatt gyárt 100 gép 100 terméket?"), és fűzd hozzá: *"Mielőtt megadnád a végső választ, lépésről lépésre, hangosan gondolkodva vezesd le a megoldást."*

* **Constraint Prompting (Szigorú kényszerítés):** A kimeneti formátum kőbe vésése.
* **Feladat:** Kérj 3 üzleti ötletet diákmunkákra, de szabd meg: *"A válaszod KIZÁRÓLAG egy Markdown táblázat lehet, 3 oszloppal (Ötlet, Költség, Időigény). Nem írhatsz bevezető szöveget, és nem írhatsz konklúziót a táblázat alá. Csak és kizárólag a táblázatot add vissza."*

### 8. Iteratív promptolás (Finomhangolás lépésről lépésre)

A prompt engineering ritkán jelent egyetlen, varázsütésszerűen tökéletes kérdést. A komplex, sokrétű problémák "egy szuszra" történő megoldása (amikor egyetlen hatalmas promptban kérünk mindent) gyakran felszínes, logikátlan vagy hibás (hallucinált) eredményt szül. A nyelvi modellekkel a leghatékonyabb munkamódszer az iteráció: a feladatot kisebb logikai lépésekre bontjuk, folyamatosan ellenőrizzük a gép kimenetét, és a kapott válaszokra reagálva pontosítjuk az irányt. Ez nemcsak megbízhatóbbá teszi az eredményt, de lehetővé teszi, hogy menet közben finomhangoljuk a részleteket.

* **Példa (Mindent egyszerre vs. Iteratív):** Rossz megközelítés (Mindent egyszerre): "Írj egy teljes üzleti tervet egy budapesti vegán pékséghez, legyen benne pénzügyi terv, marketing stratégia, versenytárselemzés és egy heti közösségi média naptár." (Az eredmény nagy valószínűséggel egy nagyon általános, klisékkel teli, felületes dokumentum lesz, kidolgozatlan számokkal).

* **Jó megközelítés (Iteratív):**
1. lépés: "Nyitni szeretnék egy vegán pékséget Budapesten. Írj 3 egyedi értékajánlatot (USP), amivel kitűnhetek a piacon." (Eredmény: A modell ad 3 ötletet).
2. lépés: "A 2-es ötlet tetszik a legjobban (cukormentes, sportolóknak szóló pékáruk). Készíts ehhez a koncepcióhoz egy részletes célközönség-profilt." (Eredmény: Célzott, releváns profil).
3. lépés: "Szuper. Ezen célközönség alapján írj egy 5 napos Instagram tartalomnaptárat, ami rájuk fókuszál." (Eredmény: Rendkívül specifikus, minőségi és koherens végeredmény, lépésről lépésre felépítve).

* **Hallgatói feladat a Geminiben:**
Próbáld ki az iteráció erejét egy adatelemzési (kódolási) problémán! Ne kérj egyszerre egy teljes, kész programot. Haladj a következő lépések szerint, és minden lépésnél várd meg az AI válaszát:
**1. Prompt:** "Írj nekem egy Python (Pandas) kódot, amely betölt egy 'sales_data.csv' nevű fájlt, és kiírja a képernyőre, hogy az egyes oszlopokban hány hiányzó adat (NaN) található."
**2. Prompt (A válasz után):** "Tegyük fel, hogy az 'Arbevetel' oszlopban talált hiányzó értékeket. Módosítsd az előző kódot úgy, hogy ezeket a hiányzó értékeket töltse fel az oszlop mediánjával!"
**3. Prompt (A válasz után):** "Tökéletes. Most adj hozzá a kódhoz egy Seaborn diagramot, ami ábrázolja a tisztított 'Arbevetel' oszlop eloszlását (histogram). A diagramnak legyen címe és tengelyfeliratai magyarul."

(Figyeld meg, mennyivel könnyebb így ellenőrizni a gép munkáját, és javítani, ha valamit elsőre rosszul értelmezett!)

---

## Konklúzió: A nyelvi modell és a kommunikáció jövője

A nyelvi modellek működése rámutat egy alapvető paradigmaváltásra a számítástechnikában: **a természetes nyelv lett az új programozási nyelv.** Amikor a Geminivel (vagy más modellel) beszélgetsz, valójában nem "chatelsz". Egy hatalmas teljesítményű szuperszámítógépet konfigurálsz, amely elképesztő adathalmazokon tanult meg mintákat felismerni.

A Prompt Engineering felismerése az, hogy a modell pontosan olyan minőségű kimenetet generál, amilyen minőségű az instrukció (Garbage In, Garbage Out). Ezek a rendszerek univerzális kommunikációs felületként (interfészként) működnek ember és gép között, ahol a szavaink jelentik az irányító kódokat.

## Old meg következő quiz-t [link](https://share.gemini.google/e5vzEai75fxt)

## Záró Reflexió (A projektfeladatodhoz)

Gondold végig a féléves saját üzleti MI projektedet.

* Hogyan tudod alkalmazni a fenti technikákat, amikor a Google Colabban végzed az Adatfeltáró Elemzést (EDA)?
* Melyik technika segítene a leginkább abban, hogy a modell ne csak kódot generáljon, hanem el is magyarázza a döntési fád működését egy menedzser számára?
* Tervezd meg fejben (vagy vázlatosan papíron), mi lenne az a System Prompt, amit beállítanál a mesterséges intelligenciának, hogy a projekted során a legjobb technikai mentorod legyen!

---