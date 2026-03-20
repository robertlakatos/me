---
title: "A mesterséges intelligencia megismerése"
collection: teaching
type: "undivided course"
permalink: /teaching/UAI
venue: "Department of Data Science and Visualization, Faculty of Informatics, University of Debrecen"
date: 2026-03-27
location: "Debrecen, Hungary"
---

Ez a 13 hetes kurzus átfogó elméleti betekintést nyújt a mesterséges intelligencia világába, kifejezetten a jövő pedagógusaira szabva. A tematika historikus íve a nyelvi fordítás klasszikus kihívásától indulva vezeti be a hallgatókat a modern gépi tanulás alapjaiba. Érintjük a legfontosabb technikai fogalmakat: az adatfeldolgozást, a tokenizációt és a vektoros reprezentációt, amely a gépi „megértés” kulcsa.

A hallgatók megismerik a különböző modell-típusokat (nyelvi, képi, hang alapú és multimodális) és az alapvető architektúrákat, mint a generatív modellek, az enkóderek és dekóderek. Kitérünk a hardveres háttérre, a GPU-gyorsítás jelentőségére, valamint a kritikus etikai kérdésekre, köztük a gépi elfogultságra (bias) és a hallucinációk kezelésére (RAG).
A kurzus záró szakasza a jövőképre fókuszál: az adaptív tanulási utakra, a fizikai valóságba kilépő robotikára (Physical AI) és a logikai következtetést ígérő szimbolikus AI-ra. A cél egy olyan szakmai szemlélet kialakítása, amely képessé teszi a tanárokat a technológia tudatos és kritikus integrálására az oktatásba. 

======

## [Email address of the Teacher](mailto:lakatos.robert@inf.unideb.hu)

## Konzultációk

- Monday / Hétfő - 14:00 - 15:30 - IK 107 (in the classroom / teremben)
- Monday / Hétfő - 15:30 - 16:00 - IK I128 (in the office / irodában)
- Monday / Hétfő - 16:00 - 17:30 - IK 204 (in the classroom / teremben)
- Monday / Hétfő - 17:30 - 18:00 - IK I128 (in the office / irodában)
- Monday / Hétfő - 18:00 - 19:30 - IK 204 (in the classroom / teremben)

- Tuesday / Kedd - 14:00 - 15:30 - IK 132 (in the classroom / teremben)
- Tuesday / Kedd - 15:30 - 16:00 - IK I128 (in the office / irodában)
- Tuesday / Kedd - 16:00 - 17:30 - IK TEOKJ II. em. 109 (in the classroom / teremben)
- Tuesday / Kedd - 17:30 - 18:00 - IK I128 (in the office / irodában)
- Tuesday / Kedd - 18:00 - 19:30 - IK TEOKJ II. em. 106 (in the classroom / teremben)

## Vizsgafeladat: „Generatív AI a regionális jövőkutatásban és társadalomföldrajzi modellezésben”

A hallgatónak egy választott magyarországi kistérség vagy vármegye társadalmi-gazdasági fenntarthatóságát kell elemeznie AI eszközökkel, és egy olyan „Digitális Régió-Víziót” alkotnia, amely alkalmas a regionális tervezés (regional planning) oktatására.

A munkafolyamat és az AI eszközök használata
1. Fázis: Regionális adatelemzés és statisztika (Gemini / Claude / ChatGPT / NotebookLM)
    - **Feladat:** A hallgató töltsön fel a Gemini-be (vagy Claude-ba) adott régióra vonatkozó KSH (Központi Statisztikai Hivatal) adatokat (pl. demográfia, munkanélküliség, vándorlási mérleg).
    - **AI funkció:** Kérje meg az AI-t, hogy azonosítsa a régió „kitörési pontjait” és a legnagyobb társadalmi kockázatokat. Alkalmazzon összehasonlító elemzést (pl. egy hátrányos helyzetű kistérség vs. a fővárosi agglomeráció).
    - **Tudományos kimenet:** Egy strukturált SWOT-analízis és egy korrelációs elemzés a regionális mutatók között.
2. Fázis: Társadalomföldrajzi vizualizáció és szimuláció (Kép- és videógenerátorok)
    - **Feladat:** A statisztikai adatok alapján a hallgató generáljon vizuális „forgatókönyveket” a régió 2050-es képéről.
    - **AI eszköz (pl. Midjourney / Runway / Kling):** Hogyan alakul át a városkép a klímaváltozás és az ipari szerkezetváltás hatására? (Pl. „Egy rozsdaövezet rehabilitációja Miskolcon, zöld technológiákkal”).
    - **Videó:** Készítsen egy videót, amely bemutatja a régió vizuális átalakulását a szocialista iparvárostól a modern technológiai központig.
    - **Tudományos kimenet:** A „Spekulatív Design” mint regionális tervezési módszertan alkalmazása.
3. Fázis: Térinformatikai (GIS) prompt-engineering
    - **Feladat:** A hallgató készíttessen a Claude-dal egy Python szkriptet, amely egy egyszerű térképi adatbázist (pl. GeoJSON) vizualizál, megjelenítve a régió specifikus problémáit (pl. iskolák elérhetősége vagy közlekedési hálózat).
    - **Tudományos kimenet:** Az AI szerepe a térinformatikai kódolás demokratizálásában az oktatás során.

## [Regional Statistics](https://www.ksh.hu/terstat_eng)

## Tudás terv

**1. hét:** Az AI hajnala és a nagy cél: A nyelvi fordítás A mesterséges intelligencia historikus megközelítése. Miért a gépi fordítás volt az eredeti "Szent Grál", és hogyan jutottunk el a szabályalapú rendszerektől a statisztikai modellekig? Az intelligencia meghatározása az oktatásban.
**2. hét:** A "nyersanyag": Adatfeldolgozás és kurátorok Az adatok útja a modellig. Az előfeldolgozás folyamata, a digitális tartalom tisztítása és a kurátorok (adatfelügyelők) szerepe. Miért nem mindegy, milyen adaton tanul a jövő nemzedéke?
**3. hét:** A nyelv matematikája: Tokenek és vektorok Hogyan látja a gép a szöveget? A tokenizáció fogalma és a vektoros reprezentáció (embeddings). Hogyan válnak a szavak és fogalmak matematikai koordinátákká egy többdimenziós térben?
**4. hét:** Mintafelismerés és jóslás: A valószínűségi gondolkodás Az AI mint statisztikai tükör. Hogyan jósolja meg a gép a következő elemet? A minták szerepe a tanulásban és a gépi "gondolkodásban". A determinisztikus vs. sztochasztikus rendszerek különbsége.
**5. hét:** Modell-típusok I.: Nyelvi és képfeldolgozó modellek Az LLM-ek (Large Language Models) és a Computer Vision alapjai. Hogyan értelmez a gép egy esszét és hogyan egy rajzot? A vizuális és szöveges információ kódolásának eltérései.
**6. hét:** Modell-típusok II.: Hangfeldolgozás és Multimodalitás A beszédfelismerés és szintézis elmélete. A multimodális modellek lényege: amikor a gép egyszerre értelmez szöveget, képet és hangot (interdiszciplináris megközelítés az oktatásban).
**7. hét:** Architektúrák: Generatív AI, Enkóder és Dekóder A Transformer modell felépítése. Mi a különbség a megértésre (Encoder) és a tartalomelőállításra (Decoder) optimalizált rendszerek között? A generatív szemlélet megjelenése a pedagógiában.
**8. hét:** A technológia fizikai korlátai: GPU és Hardware Miért a videókártya az AI "agya"? A GPU-gyorsított architektúrák jelentősége. A számítási kapacitás mint erőforrás és annak környezeti/gazdasági hatásai az iskolarendszerre.
**9. hét:** Megbízhatóság és tudásbázisok: RAG és Hallucináció Miért téved az AI, és hogyan küszöbölhető ki? A Retrieval-Augmented Generation (RAG) elmélete: a modell összekapcsolása hiteles forrásokkal (pl. tankönyvekkel). Az információhitelesség oktatása.
**10. hét:** Etika, Bias és a digitális írástudás új szintje Az algoritmusokba kódolt előítéletek (bias) elméleti háttere. Szerzői jog, adatvédelem és a hallgatók felelőssége az AI-korszakban. Hogyan alakítja át az AI az emberi kreativitás fogalmát?
**11. hét:** A jövő oktatása: Adaptív tanulás és személyre szabottság Az "egy méret mindenkinek" modell vége. Hogyan teszi lehetővé az AI az egyéni tanulási utak elméleti megalkotását? Az AI mint személyes tutor és a pedagógus megváltozott szerepköre.
**12. hét:** Physical AI: Robotika és a fizikai valóság Amikor az AI testet ölt. A környezetüket érzékelő és abba beavatkozó rendszerek. A robotika elméleti alapjai és a szenzomotoros tanulás modellezése a fizikai térben.
**13. hét:** A következő lépcsőfok: Szimbolikus AI és az AGI jelene A neurális hálózatok és a logikai (szabályalapú) rendszerek ötvözése. Elértük az általános mesterséges intelligenciát (AGI). Mit jelent majd embernek és tanárnak lenni egy gép által dominált világban?