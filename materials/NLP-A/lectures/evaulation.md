Rendben, itt van a diasor tartalmának magyarázata diáról diára, kiegészítve a szükséges fogalmakkal, hogy könnyebb legyen órát tartani belőle.

### Benchmarkolás és Értékelés

---

**1. Dia: Címlap** [cite: 1]

* **Tartalom:** Az előadás címe: "Természetes Nyelvfeldolgozás Mély Tanulással" (Natural Language Processing with Deep Learning), konkrétan a 11. előadás, amely a "Benchmarkolás és Értékelés" (Benchmarking and Evaluation) témakörével foglalkozik. Az előadó Yann Dubois.
* **Magyarázat:** Ez a dia bemutatja az előadás témáját és az előadót. A CS224N/Ling284 valószínűleg egy egyetemi kurzus kódja, amely a mély tanulás alkalmazásait tárgyalja a természetes nyelvfeldolgozás (NLP) területén.
    * **Természetes Nyelvfeldolgozás (NLP):** Az informatika és a mesterséges intelligencia azon területe, amely az emberi (természetes) nyelvek és a számítógépek közötti interakcióval foglalkozik. Célja, hogy a számítógépek képesek legyenek megérteni, értelmezni és generálni az emberi nyelvet.
    * **Mély Tanulás (Deep Learning):** A gépi tanulás egyik ága, amely mesterséges neurális hálókat használ (különösen sok réteggel rendelkezőket) adatokból való tanulásra és mintázatok felismerésére.
    * **Benchmarkolás:** Standardizált tesztek és adathalmazok használata különböző rendszerek (itt NLP modellek) teljesítményének objektív összehasonlítására.
    * **Értékelés:** Annak folyamata, hogy megmérjük, mennyire jól teljesít egy modell egy adott feladaton.

---

**2. Dia: Előadás áttekintése** [cite: 2]

* **Tartalom:** Felvázolja az előadás fő témáit:
    * Miért mérjük a teljesítményt (különböző célok).
    * Szövegosztályozás / Zárt végű feladatok értékelése.
    * Szöveggenerálás / Nyílt végű feladatok értékelése (automatikus és emberi értékelés).
    * Nagy nyelvi modellek (LLM-ek) jelenlegi értékelési módszerei.
    * Az értékeléssel kapcsolatos problémák és kihívások.
* **Magyarázat:** Ez a dia egyfajta tartalomjegyzékként szolgál, előrevetítve, hogy milyen fő pontokat fog érinteni az előadás.

---

**3. Dia: A teljesítménymérés különböző szempontjai (desiderata)** [cite: 3]

* **Tartalom:** Bemutatja, hogy a modellfejlesztés különböző fázisaiban (Tanítás, Fejlesztés, Modell kiválasztása, Bevezetés, Publikálás) más-más szempontok (desiderata) fontosak az értékelésnél.
    * **Tanítás:** Gyors, olcsó, differenciálható (matematikai értelemben, a tanuláshoz szükséges), ne legyenek "rövidítések" (a modell ne tanuljon meg egyszerű trükköket a valódi megértés helyett).
    * **Fejlesztés:** Gyors, olcsó, kerülje a rövidítéseket.
    * **Modell kiválasztása:** Gyors, olcsó.
    * **Bevezetés (Deploy):** Megbízható, feladatspecifikus, abszolút (valós teljesítményt mutató) mérőszámok.
    * **Publikálás:** Standardizált, reprodukálható, könnyen használható, viszonylag gyors, széles lefedettségű, viszonylag olcsó, akár durvább metrikák is elfogadhatók, de fontos a finom megkülönböztető képesség és a megfelelő nehézség.
* **Magyarázat:** Hangsúlyozza, hogy nincs egyetlen "legjobb" értékelési módszer; a cél határozza meg, milyen tulajdonságok a legfontosabbak egy adott metrikában.

---

**4. Dia: A benchmarkok és értékelések hajtják a fejlődést** [cite: 4, 5]

* **Tartalom:** Egy grafikon, amely bemutatja a nyelvi modellek teljesítményének (átlagos %-os pontszám az MMLU benchmarkon) javulását 2020 januárjától 2024 januárjáig. Láthatóak a különböző modellek (pl. RoBERTa, GPT-3, Chinchilla, GPT-4, Gemini Ultra) és azok teljesítménye.
* **Magyarázat:** Ez a dia azt illusztrálja, hogy a standardizált értékelési feladatok (benchmarkok) hogyan segítik elő a terület fejlődését azáltal, hogy lehetővé teszik a modellek objektív összehasonlítását és ösztönzik a jobb modellek létrehozását.
    * **MMLU (Massive Multitask Language Understanding):** Egy széles körben használt benchmark, amely különböző tudományterületekről (pl. matematika, történelem, jog, orvostudomány) származó feleletválasztós kérdésekkel méri a modellek tudását és következtetési képességét[cite: 72].
    * **Few-shot:** Olyan tanulási módszer, ahol a modellnek csak néhány példát (shots) mutatnak be egy új feladatról, és ez alapján kell általánosítania.
    * **Fine-tuned:** Egy előtanított modell további tanítása egy specifikus feladatra vagy adathalmazra.

---

**5. Dia: Két fő értékelési típus** [cite: 6, 7, 8, 9, 10, 11, 12]

* **Tartalom:** Bemutatja a két alapvető értékelési paradigmát:
    * **Zárt végű (Close-ended):** A lehetséges válaszok száma korlátozott, gyakran csak egy helyes válasz van. Példa: Szövegosztályozás (pl. hangulatelemzés: "Olvasd a könyvet, felejtsd el a filmet!" -> Negatív)[cite: 7].
    * **Nyílt végű (Open-ended):** Nagyon sok lehetséges (helyes) válasz létezik, a válaszok gyakran hosszabb szövegek. Példa: Szöveggenerálás (pl. egy történet folytatása)[cite: 8, 9, 10, 11, 12].
* **Magyarázat:** Ez a megkülönböztetés alapvető, mert a két típushoz eltérő értékelési módszerekre van szükség.

---

**6. Dia: Címlap: Zárt végű értékelés** [cite: 13]

* **Tartalom:** Csak egy cím, amely jelzi a következő szakasz témáját.

---

**7. Dia: Zárt végű feladatok jellemzői** [cite: 14]

* **Tartalom:**
    * Korlátozott számú lehetséges válasz.
    * Gyakran egy vagy csak néhány helyes válasz.
    * Lehetővé teszi az automatikus értékelést, ahogyan az a hagyományos gépi tanulásban (ML) megszokott.
* **Magyarázat:** Mivel a helyes válasz(ok) előre ismertek, könnyű automatikusan ellenőrizni, hogy a modell válasza helyes-e, és számolni a pontosságot vagy más metrikákat.
    * **Gépi Tanulás (ML) Értékelés:** Standard metrikák (pl. pontosság, precizitás, felidézés) használata annak mérésére, hogy egy modell mennyire jól teljesít egy előre definiált adathalmazon, ahol a helyes válaszok ismertek.

---

**8. Dia: Zárt végű feladatok - Példák 1** [cite: 15, 16, 17]

* **Tartalom:** Konkrét példák zárt végű NLP feladatokra:
    * **Hangulatelemzés (Sentiment analysis):** Szöveg érzelmi töltetének meghatározása (pozitív/negatív/semleges). Adathalmazok: SST, IMDB, Yelp[cite: 16].
    * **Következtetés (Entailment):** Annak eldöntése, hogy egy hipotézis logikailag következik-e egy adott szövegből (premise). Adathalmaz: SNLI[cite: 17].
    * **Névfelismerés (Named Entity Recognition, NER):** Szövegben előforduló entitások (pl. személynevek, helyek, szervezetek) azonosítása és osztályozása. Adathalmaz: CoNLL-2003.
    * **Szófajfelcímkézés (Part-of-Speech, POS tagging):** Szavak szófajának (pl. főnév, ige, melléknév) meghatározása. Adathalmaz: PTB.
* **Magyarázat:** Ezek klasszikus NLP feladatok, amelyeket gyakran használnak modellek értékelésére. Mindegyiknél viszonylag könnyen definiálható a helyes válasz.

---

**9. Dia: Zárt végű feladatok - Példák 2** [cite: 18, 19, 20, 21]

* **Tartalom:** További példák:
    * **Koreferencia-feloldás (Coreference resolution):** Annak meghatározása, hogy egy szövegben mely névmások vagy kifejezések utalnak ugyanarra az entitásra. Adathalmaz: WSC[cite: 20, 21].
    * **Kérdésválaszolás (Question Answering, QA):** Adott szöveg alapján feltett kérdésre a helyes válasz megtalálása/generálása. Itt egy példa a SQuAD 2 adathalmazból, ahol a válasz mellett "hihető" (plausible) válaszok is létezhetnek, ami bonyolítja a feladatot[cite: 19].
* **Magyarázat:** Ezek a feladatok már összetettebb nyelvi megértést igényelnek. A SQuAD 2 példa arra is rávilágít, hogy néha még a zárt végű feladatokban is lehetnek árnyalatok (pl. megválaszolhatatlan kérdések).

---

**10. Dia: Zárt végű több-feladatos benchmark - SuperGLUE** [cite: 22, 23, 24]

* **Tartalom:** Bemutatja a SuperGLUE benchmarkot, amely több különböző zárt végű feladatot foglal magában az "általános nyelvi képességek" mérésére. Egy ranglistát (leaderboard) is mutat, ahol különböző modellek (pl. Vega v2, ST-MoE-32B, PaLM 540B) teljesítményét hasonlítják össze a SuperGLUE feladatain[cite: 23]. A GLUE ennek egy korábbi, egyszerűbb változata volt[cite: 24].
* **Magyarázat:** Az ilyen több-feladatos benchmarkok célja, hogy átfogóbb képet adjanak egy modell képességeiről, mint egyetlen feladaton mért teljesítmény. A ranglisták ösztönzik a versenyt és a fejlődést.
    * **GLUE/SuperGLUE:** Széles körben elfogadott benchmark gyűjtemények NLP modellek általános nyelvi megértési képességeinek értékelésére. A SuperGLUE nehezebb feladatokat tartalmaz, mint a GLUE.

---

**11. Dia: Példák a SuperGLUE feladataiból** [cite: 25]

* **Tartalom:** Felsorolja a SuperGLUE benchmarkban szereplő feladattípusokat:
    * BoolQ, MultiRC: Szövegértés.
    * CB, RTE: Következtetés (Entailment).
    * COPA: Oki kapcsolatok felismerése.
    * ReCoRD: Kérdésválaszolás + következtetés.
    * WiC: Szavak jelentésének kontextusfüggő azonosítása.
    * WSC: Koreferencia-feloldás.
* **Magyarázat:** Részletezi, milyen konkrét képességeket mérnek a SuperGLUE benchmark részei.

---

**12. Dia: Zárt végű értékelés kihívásai** [cite: 26, 27]

* **Tartalom:** Felhívja a figyelmet a zárt végű értékelés nehézségeire:
    * **Metrikák kiválasztása:** Melyik mérőszám a legmegfelelőbb (pl. pontosság, precizitás, felidézés, F1-pontszám, ROC)?[cite: 26].
    * **Aggregálás:** Hogyan vonjunk össze több metrika vagy több feladat eredményét egyetlen pontszámmá?[cite: 26].
    * **Címkék forrása:** Honnan származnak a "helyes" válaszok, és mennyire megbízhatóak?[cite: 26].
    * **Látszólagos korrelációk (Spurious correlations):** Előfordulhat, hogy a modell nem a valódi nyelvi megértés révén, hanem valamilyen felszínes statisztikai minta (pl. egy bizonyos szó gyakori előfordulása egy adott címkével) alapján ér el jó eredményt[cite: 27].
* **Magyarázat:** Ezek a kihívások azt jelentik, hogy még a látszólag egyszerű, zárt végű értékelés sem problémamentes. Fontos kritikusan szemlélni a kapott számokat.
    * **Pontosság (Accuracy):** A helyesen osztályozott példák aránya az összes példához képest.
    * **Precizitás (Precision):** A pozitívnak jósolt példák közül hány valóban pozitív.
    * **Felidézés (Recall):** A valódi pozitív példák közül hányat talált meg a modell.
    * **F1-pontszám (F1-score):** A precizitás és a felidézés harmonikus középértéke, egyensúlyt teremt a kettő között.
    * **ROC görbe (Receiver Operating Characteristic):** Egy grafikon, amely a modell teljesítményét mutatja különböző döntési küszöbértékek mellett, általában a valódi pozitív ráta (felidézés) és a hamis pozitív ráta viszonyában.

---

**13. Dia: Látszólagos korreláció (Spurious Correlation) példa** [cite: 28, 29]

* **Tartalom:** Egy konkrét példa a látszólagos korrelációra az SNLI (következtetés) adathalmazon. Ha a hipotézisben tagadás (negation) van, az gyakran korrelál a "Negation" (ellentmondás) címkével, még akkor is, ha a következtetés valójában más (pl. "Entailment" - következmény)[cite: 29]. A modell megtanulhatja ezt a felszínes mintát ahelyett, hogy valódi logikai következtetést végezne.
* **Magyarázat:** Ez jól illusztrálja, miért veszélyesek a látszólagos korrelációk: a modell "csalhat", jó eredményt érhet el anélkül, hogy valóban megértené a feladatot.

---

**14. Dia: Címlap: Nyílt végű értékelés** [cite: 30]

* **Tartalom:** Cím, amely jelzi a következő témát.

---

**15. Dia: Nyílt végű feladatok jellemzői** [cite: 31]

* **Tartalom:**
    * Hosszú szövegek generálása.
    * Túl sok lehetséges helyes válasz van ahhoz, hogy mindet felsoroljuk.
    * Emiatt a standard ML metrikák (pl. pontosság) nem használhatók.
    * Itt már nem csak helyes/helytelen válaszokról beszélünk, hanem jobb és rosszabb válaszokról.
    * Példák: Összefoglalás (Summarization - CNN-DM, Gigaword adathalmazok), Fordítás (Translation - WMT benchmark), Utasításkövetés (Instruction-following - Chatbot Arena, AlpacaEval, MT-Bench benchmarkok).
* **Magyarázat:** A nyílt végű feladatok értékelése sokkal nehezebb, mert nincs egyértelmű "helyes" válasz. Az értékelésnek inkább a generált szöveg minőségére (pl. folyékonyság, relevancia, koherencia) kell összpontosítania.
    * **Szövegösszefoglalás (Summarization):** Hosszabb szöveg lényegének rövid, tömör megfogalmazása.
    * **Gépi Fordítás (Machine Translation):** Szöveg átültetése egyik nyelvről a másikra.
    * **Utasításkövetés (Instruction Following):** A modell képessége arra, hogy végrehajtson egy adott szöveges utasítást.

---

**16. Dia: Értékelési módszerek szöveggenerálásra** [cite: 32, 33]

* **Tartalom:** Három fő kategóriába sorolja a nyílt végű feladatok értékelési módszereit:
    * **Tartalmi átfedési metrikák (Content Overlap Metrics):** A generált és egy referencia szöveg szókincsbeli hasonlóságát mérik.
    * **Modell alapú metrikák (Model-based Metrics):** Tanult reprezentációkat használnak a szemantikai hasonlóság mérésére.
    * **Emberi értékelések (Human Evaluations):** Emberek értékelik a generált szöveg minőségét.
* **Magyarázat:** Ez a dia bevezeti a nyílt végű értékelés konkrét technikáit.

---

**17. Dia: Tartalmi átfedési metrikák** [cite: 34, 35]

* **Tartalom:**
    * A generált szöveg és egy "arany standard" (gold-standard, általában ember által írt referencia) szöveg közötti lexikai (szókincsbeli) hasonlóságot mérik[cite: 34].
    * Gyorsak és hatékonyak[cite: 34].
    * Példák: N-gram átfedési metrikák (BLEU, ROUGE, METEOR, CIDEr)[cite: 34].
    * Nem ideálisak, de fordításnál és összefoglalásnál még mindig gyakran használják őket[cite: 34].
    * A példa ("Ref: They walked to the grocery store.", "Gen: The woman went to the hardware store.") illusztrálja a precizitást (precision) és felidézést (recall) a szavak szintjén[cite: 35].
* **Magyarázat:** Ezek a metrikák azt mérik, hogy a generált szövegben szereplő szavak vagy szósorozatok (n-grammok) mennyire fedik át a referencia szövegben lévőket. Olcsó és gyors, de korlátozott módszer.
    * **Arany Standard (Gold Standard):** Egy referencia adathalmaz vagy válasz, amelyet általában emberek hoznak létre, és amelyhez a modell teljesítményét viszonyítják.
    * **N-gram:** Egy szövegben egymást követő 'n' darab elem (általában szó) sorozata. Pl. "a nagy kutya" egy 3-gram.
    * **BLEU (Bilingual Evaluation Understudy):** Elsősorban gépi fordítás értékelésére használt metrika, amely a generált szöveg n-grammjainak precizitását méri a referencia fordítás(ok)hoz képest.
    * **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** Elsősorban szövegösszefoglalás értékelésére használt metrikacsalád, amely a generált szöveg n-grammjainak felidézését méri a referencia összefoglaló(k)hoz képest.

---

**18. Dia: Egyszerű hibaeset (tartalmi átfedés)** [cite: 36, 37]

* **Tartalom:** Bemutatja, hogy az n-gram átfedési metrikák nem értik a jelentést (szemantikát). Egy kérdésre ("Élvezed a CS224N előadásokat?") adott, jelentésükben ellentétes válaszok ("Heck yes!" - Naná!; "Heck no!" - Fenét!) hasonlóan magas pontszámot kaphatnak, ha csak a szavak átfedését nézzük egy pozitív referenciához ("Heck yes!") képest[cite: 37]. A "Yup." alacsony pontszámot kap (false negative - téves negatív), míg a "Heck no!" magasat (false positive - téves pozitív).
* **Magyarázat:** Ez a fő kritika ezekkel a metrikákkal szemben: csak a felszínt, a szavak egyezését nézik, a mögöttes jelentést nem.
    * **Szemantika:** A szavak és mondatok jelentésével foglalkozó tudományág.

---

**19. Dia: Modell alapú metrikák a szemantika jobb megragadására** [cite: 38]

* **Tartalom:**
    * Tanult szó- és mondatreprezentációkat (beágyazásokat - embeddings) használnak a generált és referencia szövegek közötti szemantikai (jelentésbeli) hasonlóság kiszámítására.
    * Az embeddingek előtanítottak, a hasonlóság mérésére használt távolságmetrikák fixek lehetnek.
* **Magyarázat:** Ezek a metrikák megpróbálják figyelembe venni a szavak jelentését is, nem csak a formai egyezést.
    * **Beágyazás (Embedding):** Szavak, mondatok vagy más adatelemek numerikus (vektoriális) reprezentációja egy többdimenziós térben, ahol a hasonló jelentésű elemek közel helyezkednek el egymáshoz.
    * **Szemantikai Hasonlóság:** Annak mértéke, hogy két szövegrészlet mennyire hasonló jelentéssel bír.

---

**20. Dia: Modell alapú metrikák: Szótávolság függvények** [cite: 39, 40, 41]

* **Tartalom:** Példák modell alapú metrikákra:
    * **Vektor hasonlóság alapúak:** Embedding Average, Vector Extrema, MEANT, YISI - ezek a szóbeágyazásokból számolnak hasonlóságot[cite: 40].
    * **BERTSCORE:** Előtanított BERT kontextuális beágyazásokat használ, és a jelölt és referencia mondatok szavait koszinusz hasonlóság alapján párosítja össze[cite: 41].
* **Magyarázat:** Konkrét példák olyan metrikákra, amelyek a szavak vagy mondatok tanult reprezentációi közötti távolságot/hasonlóságot mérik.
    * **BERT (Bidirectional Encoder Representations from Transformers):** Egy népszerű, transzformátor architektúrán alapuló nyelvi modell, amelyet gyakran használnak szövegek kontextuális beágyazásainak létrehozására.
    * **Koszinusz Hasonlóság (Cosine Similarity):** Két vektor közötti szöget méri; magas érték (1-hez közeli) jelzi, hogy a vektorok iránya hasonló (azaz a reprezentált elemek jelentése is hasonló lehet).

---

**21. Dia: Modell alapú metrikák: Túl a szóegyezésen** [cite: 42, 43]

* **Tartalom:**
    * **BLEURT:** Egy BERT alapú regressziós modell, amely egy pontszámot ad vissza. Ez a pontszám azt jelzi, hogy a jelölt szöveg mennyire nyelvtanilag helyes és mennyire adja át a referencia szöveg jelentését[cite: 43].
* **Magyarázat:** A BLEURT egy fejlettebb modell alapú metrika, amely nemcsak a szavak párosítására támaszkodik, hanem egy tanult modell segítségével értékeli a generált szöveg általános minőségét (nyelvtaniság, jelentéshűség).
    * **Regressziós Modell:** Olyan gépi tanulási modell, amely folytonos kimeneti értéket (itt egy minőségi pontszámot) jósol meg bemeneti adatok alapján.
    * **Nyelvtaniság (Grammaticality):** Annak mértéke, hogy egy szöveg megfelel-e egy adott nyelv nyelvtani szabályainak.

---

**22. Dia: Fontos hibaeset (referencia alapú metrikák)** [cite: 44, 45]

* **Tartalom:** A referencia alapú mértékek (legyen az tartalmi átfedés vagy modell alapú) csak annyira jók, amennyire a referenciáik[cite: 44]. Ha a használt referencia (pl. egy átlagos ember által írt szöveg) nem korrelál jól a szakértői (emberi) ítéletekkel, akkor a metrika sem fog[cite: 45].
* **Magyarázat:** Hiába van egy kifinomult metrikánk, ha rossz vagy nem reprezentatív referencia szöveghez hasonlítjuk a modell kimenetét, az eredmény félrevezető lesz. A referencia minősége kulcsfontosságú.

---

**23. Dia: Referencia nélküli (Reference-free) értékelések** [cite: 46]

* **Tartalom:**
    * **Referencia alapú:** Ember által írt referenciához hasonlítja a modell kimenetét (pl. BLEU, ROUGE, BertScore). Ez volt a standard.
    * **Referencia nélküli:** Nincs szükség emberi referenciára. Egy másik modell (gyakran egy erős LLM, mint a GPT-4) ad pontszámot a generált kimenetre. Régen nem volt standard, de az LLM-ekkel egyre népszerűbbé válik. Példák: AlpacaEval, MT-Bench.
* **Magyarázat:** Ez egy újabb paradigma, ahol megpróbáljuk kiiktatni az emberi referencia szükségességét, és egy másik AI modellt használunk bírálóként. Ennek előnye lehet a sebesség és az alacsonyabb költség, de megvannak a maga kihívásai (pl. a bíráló modell elfogultsága).

---

**24. Dia: Emberi értékelések** [cite: 47, 48]

* **Tartalom:**
    * Az automatikus metrikák gyakran nem tükrözik tökéletesen az emberi ítéleteket[cite: 47].
    * Az emberi értékelés a legfontosabb értékelési forma a szöveggenerálásnál, ez az "arany standard"[cite: 47, 48].
    * Az új automatikus metrikáknak jól kell korrelálniuk az emberi értékelésekkel[cite: 48].
* **Magyarázat:** Bár költséges és lassú, végül az emberi ítélet az, ami igazán számít, különösen a nyílt végű, kreatív feladatoknál. Az automatikus metrikák csak közelítések.

---

**25. Dia: Emberi értékelések - Részletek** [cite: 49]

* **Tartalom:**
    * Emberek értékelik a generált szöveg minőségét, akár általánosságban, akár specifikus dimenziók mentén:
        * **Folyékonyság (fluency):** Mennyire természetes és olvasható a szöveg.
        * **Koherencia / Konzisztencia (coherence / consistency):** Mennyire logikus és ellentmondásmentes a szöveg.
        * **Tényszerűség / Helyesség (factuality / correctness):** Mennyire pontosak a közölt információk.
        * **Józan ész (commonsense):** Mennyire felel meg a szöveg a józan észnek és a világ működéséről alkotott alapvető tudásunknak.
        * **Stílus / Formalitás (style / formality):** Megfelel-e a szöveg stílusa a kontextusnak.
        * **Nyelvtaniság (grammaticality):** Mennyire helyes nyelvtanilag.
        * **Redundancia (redundancy):** Ismétel-e feleslegesen információkat.
    * Fontos megjegyzés: Különböző tanulmányokban végzett emberi értékelések pontszámai nem hasonlíthatók össze közvetlenül, még ha ugyanazokat a dimenziókat is mérték látszólag!
* **Magyarázat:** Részletezi, milyen szempontok szerint értékelhetik emberek a generált szöveget. Hangsúlyozza az összehasonlíthatóság nehézségét a különböző értékelési eljárások miatt.

---

**26. Dia: Emberi értékelés: Problémák** [cite: 50]

* **Tartalom:** Bár az emberi értékelés az arany standard, megvannak a maga problémái:
    * Lassú.
    * Drága.
    * Értékelők közötti véleménykülönbség (Inter-annotator disagreement), főleg szubjektív kérdésekben.
    * Ugyanazon értékelő véleményének változása az idő múlásával (Intra-annotator disagreement).
    * Nem reprodukálható könnyen.
    * Inkább a precizitást méri (a bemutatott elemek minőségét), mint a felidézést (minden lehetséges jó kimenet lefedését).
    * Elfogultságok/rövidítések, ha az ösztönzők nincsenek jól beállítva (pl. a cél a minél több értékelés óránként a minőség helyett).
    * Idézet: Az emberi értékeléseknek csak kb. 5%-a megismételhető (azaz minden információ nyilvános a kísérlet újrafuttatásához), és ez is csak kb. 20%-ra nő, ha a szerzők segítségét kérik.
* **Magyarázat:** Felsorolja az emberi értékelés gyakorlati nehézségeit és korlátait.
    * **Értékelők közötti egyetértés (Inter-annotator agreement):** Annak mértéke, hogy több ember mennyire ért egyet ugyanazon elem értékelésében. Alacsony érték szubjektivitásra vagy rosszul definiált feladatra utalhat.

---

**27. Dia: Emberi értékelés: További problémák** [cite: 51, 52, 53]

* **Tartalom:** További kihívások:
    * Hogyan írjuk le pontosan az értékelési feladatot?[cite: 51].
    * Hogyan jelenítsük meg a feladatot az értékelőknek (felület, instrukciók)?[cite: 52].
    * Milyen metrikát használjunk (pl. skála, rangsorolás)?[cite: 52].
    * Hogyan válasszuk ki az értékelőket (szakértelem, demográfia)?[cite: 53].
    * Hogyan monitorozzuk az értékelőket (időráfordítás, pontosság, konzisztencia)?[cite: 53].
* **Magyarázat:** Ezek a gyakorlati megvalósítás kérdései, amelyek mind befolyásolják az emberi értékelés megbízhatóságát és érvényességét.

---

**28. Dia: Referencia nélküli értékelés: Chatbotok** [cite: 54, 55, 56]

* **Tartalom:** Hogyan értékeljünk egy olyan komplex rendszert, mint a ChatGPT?[cite: 54].
    * Nehéz, mert rengeteg különböző felhasználási módja van[cite: 55].
    * A válaszok hosszúak, ami tovább nehezíti az értékelést[cite: 55].
    * Gyakori módszer a két modell kimenetének egymás melletti összehasonlítása (side-by-side)[cite: 56].
* **Magyarázat:** Az olyan sokoldalú és nyílt végű modellek, mint a chatbotok, különösen nagy kihívást jelentenek az értékelés szempontjából.

---

**29. Dia: Egymás melletti (Side-by-side) értékelés** [cite: 57]

* **Tartalom:** Egy illusztráció arról, hogyan működik ez: az ember megkapja ugyanazt a kérdést/promptot, és két különböző modell által generált választ. Ezután szavaznia kell, melyik a jobb (pl. egy felfelé vagy lefelé mutató hüvelykujjal).
* **Magyarázat:** Ez egy relatív értékelési módszer, amely azt méri, hogy az emberek melyik modellt preferálják egy adott feladatra.

---

**30. Dia: Mi hiányzik az egymás melletti emberi értékelésből?** [cite: 58]

* **Tartalom:** Bár ez a jelenlegi arany standard a chat LLM-ek értékelésére, vannak korlátai:
    * **Külső érvényesség (External validity):** Az, hogy az emberek hogyan értékelnek egy dedikált weboldalon, nem biztos, hogy reprezentálja a valós felhasználási szokásokat és preferenciákat.
    * **Költség:** Az emberi annotáció drága és időigényes, nagy közösségi erőfeszítést igényel. Az új modellek benchmarkolása sokáig tart, és csak a legjelentősebb modelleket értékelik így.
* **Magyarázat:** Rámutat ennek a népszerű módszernek a gyakorlati és módszertani korlátaira.

---

**31. Dia: Költségek csökkentése – LM használata értékelőként** [cite: 59]

* **Tartalom:** Az ötlet: használjunk egy erős nyelvi modellt (LM) referencia nélküli értékelőként. Meglepően magas korrelációt mutat az emberi ítéletekkel. Népszerű verziók: AlpacaEval, MT-bench. A modellnek kell eldöntenie, hogy két másik modell kimenete közül melyik a jobb.
* **Magyarázat:** Ez visszatér a 23. dián bemutatott referencia nélküli értékeléshez, ahol egy AI modell "bírálja" egy másik AI modell munkáját, potenciálisan olcsóbban és gyorsabban, mint az emberek.

---

**32. Dia: AlpacaFarm: Egyezés az emberi értékeléssel** [cite: 60]

* **Tartalom:** Az AlpacaFarm projekt eredményei szerint az LM-alapú értékelés 100x olcsóbb, 100x gyorsabb és magasabb egyetértést mutat (azaz konzisztensebb), mint az emberek. Megjegyzés: ez a módszer használható RLAIF-hez is.
* **Magyarázat:** Erős állítások az LM-alapú értékelés előnyeiről.
    * **RLAIF (Reinforcement Learning from AI Feedback):** Megerősítéses tanulás AI visszajelzésből. Olyan technika, ahol egy AI modellt (az értékelőt) használnak jutalomjelzések generálására egy másik AI modell (a tanítandó modell) tanításához, az emberi visszajelzés helyett vagy mellett.

---

**33. Dia: AlpacaFarm: Emberi egyetértés alacsony oka** [cite: 61]

* **Tartalom:** Az emberek közötti alacsony egyetértés oka a nagy variancia (eltérés) az ítéleteikben.
* **Magyarázat:** Az emberek szubjektívebbek, kevésbé konzisztensek, mint egy determinisztikusabb (vagy legalábbis konzisztensebben működő) LM értékelő.

---

**34. Dia: Mire figyeljünk (LM értékelőknél)** [cite: 62, 63]

* **Tartalom:** Ugyanazok a problémák merülhetnek fel, mint korábban:
    * **Látszólagos korrelációk!**[cite: 62].
    * **Hosszúság (Length bias):** Az LM értékelő preferálhatja a hosszabb válaszokat, függetlenül a minőségtől[cite: 63].
    * **Pozíció (Position bias):** Az értékelő preferálhatja az elsőként vagy másodikként bemutatott választ (ezt általában véletlenszerűsítéssel kiküszöbölik)[cite: 63].
    * **GPT-4 ön-elfogultság (self-bias):** A GPT-4, mint értékelő, hajlamos lehet a saját maga által generált (vagy ahhoz hasonló stílusú) válaszokat preferálni[cite: 63].
* **Magyarázat:** Figyelmeztet, hogy az LM-alapú értékelés sem csodaszer, megvannak a maga potenciális torzításai, amelyeket figyelembe kell venni.

---

**35. Dia: AlpacaEval** [cite: 64]

* **Tartalom:**
    * Az Alpaca modell fejlesztéséhez használt belső benchmark volt.
    * Állítólag 98%-os korrelációt mutat a Chatbot Arena (emberi preferencián alapuló ranglista) eredményeivel.
    * Gyors (< 3 perc) és olcsó (< $10) egy modell értékelése.
    * **Működése:**
        1.  Minden utasításra generál egy választ a referencia (baseline) modell és az értékelendő modell.
        2.  Megkérdezik a GPT-4-et, mi a valószínűsége, hogy az értékelendő modell válasza jobb.
        3.  (AlpacaEval LC - Length Controlled): Újrasúlyozzák a győzelmi valószínűséget a kimenetek hossza alapján.
        4.  Átlagolják a győzelmi valószínűségeket -> ez adja a győzelmi arányt (win rate).
* **Magyarázat:** Részletezi az egyik népszerű LM-alapú értékelési keretrendszer, az AlpacaEval működését.

---

**36. Dia: AlpacaEval: Rendszerszintű korreláció** [cite: 65]

* **Tartalom:** Egy grafikon, amely vizuálisan is megerősíti az AlpacaEval (LM-értékelő) és a Chatbot Arena (emberi értékelés) közötti magas korrelációt rendszerszinten (azaz a modellek rangsorolásában).
* **Magyarázat:** Ez az adat támasztja alá az LM-alapú értékelés létjogosultságát, mivel jól közelíti az emberi preferenciákat.

---

**37. Dia: AlpacaEval Hosszúság-Kontrollált (Length Controlled)** [cite: 66]

* **Tartalom:** Példa a látszólagos korreláció (itt: hosszúság-torzítás) kezelésére. Megbecsüli, mi lenne a metrika értéke (győzelmi arány), ha a referencia és a modell kimenetei azonos hosszúságúak lennének.
* **Magyarázat:** Ez egy finomítás, amely megpróbálja kiszűrni azt a hatást, hogy az értékelő LM esetleg csak azért preferál egy választ, mert hosszabb.

---

**38. Dia: Ön-elfogultság (Self-bias)** [cite: 67]

* **Tartalom:** Az értékelő (pl. GPT-4) elfogult lehet a saját kimenetei (vagy az ahhoz hasonló stílusú kimenetek) iránt, de állítólag meglepően kis mértékben.
* **Magyarázat:** Elismeri az ön-elfogultság létezését, de kisebbíti annak jelentőségét az LM-alapú értékelőknél.

---

**39. Dia: Címlap: LLM-ek jelenlegi értékelése** [cite: 68]

* **Tartalom:** Cím, amely az LLM-ek értékelésének jelenlegi gyakorlatát vezeti be.

---

**40. Dia: LLM-ek jelenlegi értékelése - Áttekintés** [cite: 69]

* **Tartalom:** Három fő megközelítést emel ki az LLM-ek értékelésében:
    * **Perplexitás (Perplexity):** Főleg az előtanítás (pretraining) fázisában használják a modell alapvető nyelvi modellezési képességének mérésére.
    * **"Minden" (Everything):** Átfogó benchmark gyűjtemények (pl. HELM, Open LLM Leaderboard) használata a finomhangolt (finetuned) modellek széles körű képességeinek mérésére.
    * **Aréna-szerű (Arena-like):** Emberi preferenciákon alapuló összehasonlító értékelések (pl. Chatbot Arena).
* **Magyarázat:** Összefoglalja a modern LLM-ek értékelésének bevett módszereit.
    * **Előtanítás (Pretraining):** Az a folyamat, amikor egy nagy nyelvi modellt hatalmas mennyiségű szöveges adaton tanítanak általános nyelvi mintázatok elsajátítására, mielőtt specifikus feladatokra finomhangolnák.
    * **Finomhangolás (Fine-tuning):** Egy előtanított modell további tanítása egy kisebb, specifikusabb adathalmazon, hogy jobban teljesítsen egy adott feladaton.

---

**41. Dia: "Minden": HELM és Open LLM Leaderboard** [cite: 70]

* **Tartalom:** Két példa az átfogó benchmark gyűjteményekre:
    * **HELM (Holistic Evaluation of Language Models):** Stanford által fejlesztett keretrendszer, amely sok különböző, automatikusan értékelhető benchmarkot gyűjt össze és értékel ki rajtuk modelleket.
    * **HuggingFace Open LLM Leaderboard:** Egy nyilvános ranglista, amely szintén sok benchmarkon méri és hasonlítja össze a nyílt forráskódú LLM-ek teljesítményét.
* **Magyarázat:** Ezek a platformok próbálják szabványosítani és széles körben mérni az LLM-ek képességeit számos különböző feladaton keresztül.

---

**42. Dia: Mik a gyakori LM adathalmazok?** [cite: 71]

* **Tartalom:** Egy szófelhő (word cloud) mutatja, hogy a benchmarkok milyen sokféle adathalmazt és feladatot tartalmaznak (pl. MMLU, ARC, HellaSwag, Winogrande, BoolQ, SQuAD, TriviaQA, stb.).
* **Magyarázat:** Illusztrálja az értékeléshez használt feladatok sokféleségét.

---

**43. Dia: Visszatekintés: MMLU** [cite: 72]

* **Tartalom:** Ismét megemlíti az MMLU (Massive Multitask Language Understanding) benchmarkot, hangsúlyozva, hogy 57 különböző, tudásintenzív feladatot tartalmaz az LM-ek teljesítményének mérésére.
* **Magyarázat:** Emlékeztető az egyik legfontosabb és legátfogóbb tudásalapú benchmarkról.

---

**44. Dia: Néhány intuíció: példák az MMLU-ból** [cite: 73]

* **Tartalom:** Konkrét példákat mutat be az MMLU-ban szereplő kérdéstípusokra különböző területekről (pl. középiskolai matematika, amerikai történelem, informatika, szakmai jog, stb.).
* **Magyarázat:** Ízelítőt ad abból, milyen típusú tudást és következtetési képességet mér az MMLU.

---

**45. Dia: Egyéb képességek: Kódgenerálás** [cite: 74]

* **Tartalom:** Az LLM-ek kódgenerálási képességének értékelése.
    * **HumanEval:** Egy benchmark, ahol emberek által írt programozási feladatokat kell megoldaniuk a modelleknek.
    * **Értékelés:** A generált kód futtathatóságát és helyességét tesztesetekkel (test cases) ellenőrzik.
    * **Metrika:** Pass@k - Azt méri, hogy a modell által generált 'k' számú megoldási javaslat közül legalább egy sikeresen átmegy-e az összes teszteseten. (Pl. Pass@1: az elsőként generált megoldás sikeres-e). GPT-4 itt kb. 67%-os Pass@1 értéket ért el.
* **Magyarázat:** Bemutatja, hogy az LLM-eket nem csak szöveges feladatokra, hanem például programkód generálására is értékelik, ahol az értékelés objektívebb lehet a tesztesetek miatt.
    * **Kódgenerálás:** Forráskód automatikus létrehozása természetes nyelvi leírás vagy más specifikáció alapján.
    * **Tesztesetek:** Előre definiált bemenetek és elvárt kimenetek egy programhoz, amelyek segítségével ellenőrizhető annak helyes működése.

---

**46. Dia: Egyéb képességek: Ágensek** [cite: 75, 76]

* **Tartalom:** Az LLM-eket gyakran használják ágensek "agyaként", amelyek cselekedni tudnak a világban (pl. szoftvereket kezelnek, információt keresnek). Az ilyen ágensek értékelése kihívást jelent, és gyakran "homokozó" (sandbox) környezetekben kell végezni a biztonság és reprodukálhatóság érdekében[cite: 76].
* **Magyarázat:** Kitér az LLM-ek egy újabb alkalmazási területére (ágensek vezérlése) és az ezzel járó speciális értékelési nehézségekre.
    * **AI Ágens:** Olyan autonóm entitás, amely érzékeli a környezetét és cselekszik benne céljai elérése érdekében.
    * **Homokozó (Sandbox) Környezet:** Elszigetelt tesztkörnyezet, ahol a programok vagy ágensek biztonságosan futtathatók anélkül, hogy kárt okoznának a valódi rendszerben.

---

**47. Dia: Perplexitás** [cite: 77]

* **Tartalom:**
    * A perplexitás (zavarosság) egy mérőszám, amely szorosan korrelál a modell későbbi (downstream) feladatokon nyújtott teljesítményével.
    * Értéke azonban függ a használt adattól és a tokenizálótól.
* **Magyarázat:** A perplexitás azt méri, mennyire "meglepő" egy adott szöveg a modell számára. Alacsonyabb perplexitás azt jelenti, hogy a modell jobban tudja előre jelezni a következő szót/tokent, ami általában jobb nyelvi modellezési képességre utal. Fontos tudni, hogy értéke nem abszolút, csak azonos tokenizáló és adathalmaz esetén hasonlítható össze.
    * **Perplexitás:** Információelméleti mérőszám, amely azt mutatja, átlagosan hány lehetséges választás (szó/token) közül "választ" a modell a szöveg generálása/feldolgozása során. Minél alacsonyabb, annál jobb a modell.
    * **Tokenizáló (Tokenizer):** Az a komponens, amely a bemeneti szöveget kisebb egységekre, ún. tokenekre bontja (amik lehetnek szavak, szó-részek vagy karakterek), amelyeket a modell fel tud dolgozni. A tokenizálás módja befolyásolja a perplexitás értékét.

---

**48. Dia: ⚔️ Aréna-szerű (Arena-like)** [cite: 78]

* **Tartalom:** Visszautal az emberi preferenciákon alapuló értékelésre: "Hagyjuk, hogy a felhasználók döntsenek!" - azaz az emberek közvetlen összehasonlításban mondják meg, melyik modell teljesít jobban.
* **Magyarázat:** Ez a megközelítés a felhasználói élményt és preferenciát helyezi előtérbe, ami különösen fontos a felhasználókkal közvetlenül interakcióba lépő modelleknél (pl. chatbotok).

---

**49. Dia: Címlap: Problémák és kihívások az értékeléssel** [cite: 79]

* **Tartalom:** Cím, amely jelzi a következő szakaszt, ami az értékelés nehézségeit és buktatóit tárgyalja. Egy linket is megad további olvasnivalóhoz (Ruder.io blog).

---

**50. Dia: Konzisztencia problémák** [cite: 80]

* **Tartalom:** Egy ábra, amely illusztrálja, hogy ugyanazon modell (pl. GPT-3.5) teljesítménye jelentősen eltérhet ugyanazon a benchmarkon (MMLU) attól függően, hogy pontosan hogyan implementálják az értékelést (pl. milyen promptot használnak).[cite: 80].
* **Magyarázat:** Már kis különbségek is az értékelési protokollban (pl. a kérdés megfogalmazása) nagy eltéréseket okozhatnak az eredményekben, megnehezítve a modellek megbízható összehasonlítását.

---

**51. Dia: Konzisztencia problémák: MMLU** [cite: 81, 82]

* **Tartalom:** Konkrét példák az MMLU benchmark implementációs különbségeire[cite: 81]:
    * Különböző promptok (a kérdés és a válaszlehetőségek formátuma).
    * Különböző generálási módszerek (hogyan nyeri ki a modell a választ).
    * Hogyan választják ki a legvalószínűbb választ (pl. a generált válasz valószínűsége alapján [cite: 81] vs. a lehetséges válaszok közül a legvalószínűbb kiválasztása [cite: 82]).
* **Magyarázat:** Részletezi, milyen technikai különbségek okozhatnak inkonzisztenciát az MMLU eredményekben.

---

**52. Dia: Kontamináció és Túlilleszkedés (Overfitting) problémák** [cite: 83]

* **Tartalom:**
    * **Kontamináció (Contamination):** Előfordulhat, hogy a benchmarkok tesztadatai (vagy azok részei) véletlenül vagy szándékosan bekerültek a modell tanítóadataiba. Ez mesterségesen javítja a modell teljesítményét az adott benchmarkon. Különösen nehéz ellenőrizni zárt forráskódú modelleknél.
    * **Túlilleszkedés (Overfitting):** A modellek túlságosan "rágyúrhatnak" egy specifikus benchmarkra, megtanulva annak sajátosságait ahelyett, hogy általános képességeket sajátítanának el.
* **Magyarázat:** Két komoly probléma, amely megkérdőjelezheti a benchmark eredmények valódiságát és általánosíthatóságát.
    * **Adatkontamináció:** A tesztadatok (amelyeken a modell teljesítményét mérni kellene) valamilyen formában jelen vannak a tanítóadatok között, így a modell "előre tudja" a válaszokat.
    * **Túlilleszkedés:** Az a jelenség, amikor egy modell túlságosan jól megtanulja a tanítóadatok sajátosságait (beleértve a zajt is), és emiatt rosszul általánosít új, korábban nem látott adatokra.

---

**53. Dia: Túlilleszkedés probléma (következmény)** [cite: 84]

* **Tartalom:** A modellek túl gyorsan érik el az "emberi szintű" teljesítményt a benchmarkokon. Ez vagy azt jelenti, hogy a benchmark túl könnyűvé vált, vagy azt, hogy a modellek túilleszkedtek rá.
* **Magyarázat:** Ha a modellek könnyedén kimaxolnak egy benchmarkot, az már nem alkalmas a jobb modellek megkülönböztetésére, és elveszti értékelő szerepét.

---

**54. Dia: Túlilleszkedés enyhítése** [cite: 85]

* **Tartalom:** Hogyan lehet csökkenteni a túlilleszkedés veszélyét?
    * **Privát teszthalmaz:** A tesztadatokat titokban tartják, és csak korlátozott számú alkalommal engedik a modelleket rajtuk kiértékelni.
    * **Dinamikus teszthalmaz:** Folyamatosan változtatják a bemeneteket, új feladatokat adnak hozzá, hogy a modellek ne tudjanak egy statikus halmazra optimalizálni. Az "Aréna" (⚔️) szimbólum utalhat az ilyen dinamikus, versenyalapú értékelésekre.
* **Magyarázat:** Módszerek a benchmarkok "frissen tartására" és a túlilleszkedés megnehezítésére.

---

**55. Dia: Kontamináció enyhítése: Detektorok** [cite: 86, 87]

* **Tartalom:** Módszerek annak észlelésére, hogy egy modellt valószínűleg egy adott benchmarkon tanítottak-e:
    * **Min-k-prob / Exchangeability test:** Statisztikai tesztek, amelyek azt vizsgálják, hogy a modell által adott valószínűségek a benchmark adatokra "túl magasak"-e[cite: 87], vagy hogy a modell felismeri-e az adathalmaz olyan specifikus sorrendi információit, amit csak akkor tanulhatott meg, ha látta az egész adathalmazt[cite: 87]. Ezek gyakran heurisztikusak (közelítő szabályokon alapulnak)[cite: 87].
* **Magyarázat:** Technikák a rejtett kontamináció felderítésére, bár ezek sem mindig tökéletesek.

---

**56. Dia: Az NLP benchmarkolás monokultúrája** [cite: 88]

* **Tartalom:** Kritika: a legtöbb kutatás és értékelés szinte kizárólag az angol nyelvre és a teljesítményre (pl. pontosságra) koncentrál, figyelmen kívül hagyva más nyelveket és más fontos szempontokat (pl. hatékonyság, torzítások).
* **Magyarázat:** Felhívja a figyelmet az értékelési gyakorlatok beszűkültségére és az ebből fakadó problémákra (pl. az angoltól eltérő nyelvekre fejlesztett modellek alulértékelése).

---

**57. Dia: Többnyelvű benchmarkolás** [cite: 89, 90]

* **Tartalom:** Hangsúlyozza, hogy léteznek többnyelvű benchmarkok, és ezeket használni kellene! Példák:
    * MEGA: Generatív AI többnyelvű értékelése (16 adathalmaz, 70 nyelv)[cite: 89].
    * GlobalBench: (966 adathalmaz, 190 nyelv)[cite: 89].
    * XTREME: Többnyelvű, több-feladatos benchmark a nyelvek közötti általánosítás értékelésére (9 feladat, 40 nyelv)[cite: 90].
    * MMLUE benchmark (MMLU / ARC / HellaSwag 26 nyelvre lefordítva)[cite: 90].
* **Magyarázat:** Bemutatja a megoldást a monokultúra problémájára: létező, több nyelvet lefedő értékelési keretrendszerek használata.

---

**58. Dia: Reduktív egymetrikás probléma** [cite: 91]

* **Tartalom:** Kritika: A teljesítmény (pl. pontosság) nem minden. Más fontos szempontokat is figyelembe kellene venni:
    * Számítási hatékonyság.
    * Torzítások (biases).
    * Méltányosság (fairness).
    * Az eredmények átlagolása elfedheti a kisebbségi csoportokra vagy eltérő preferenciájú felhasználókra vonatkozó gyenge teljesítményt.
* **Magyarázat:** Figyelmeztet, hogy a modellek értékelésekor ne csak egyetlen számra (pl. átlagos pontosság) koncentráljunk, mert az nem ad teljes képet, és elfedhet fontos problémákat.

---

**59. Dia: Vegyük figyelembe a számítási hatékonyságot** [cite: 92]

* **Tartalom:** Példa egy olyan benchmarkra, amely a hatékonyságot is méri:
    * **MLPerf:** Azt méri, mennyi időbe telik egy modellnek elérni egy kívánt minőségi célt.
* **Magyarázat:** Konkrét példa arra, hogyan lehet a puszta pontosságon túl más fontos szempontokat (itt: sebesség/erőforrásigény) is mérni.
    * **Számítási Hatékonyság:** Mennyi számítási erőforrást (pl. idő, memória, energia) igényel egy modell tanítása vagy futtatása.

---

**60. Dia: Vegyük figyelembe a torzításokat** [cite: 93]

* **Tartalom:** Példa egy olyan benchmarkra, amely a torzításokat vizsgálja:
    * **DiscrimEval:** Sablon alapú megközelítés. Azt vizsgálja, hogyan változik a modell döntése, ha a bemenetben szereplő személy vagy csoport jellemzőit (pl. nem, etnikum) megváltoztatjuk.
* **Magyarázat:** Bemutat egy módszert a modellekben rejlő társadalmi torzítások feltárására és mérésére.
    * **Torzítás AI-ban (Bias in AI):** Rendszerszintű, tisztességtelen megkülönböztetés vagy előítélet, amely a modell döntéseiben vagy kimeneteiben megjelenik, gyakran a tanítóadatokban lévő torzítások vagy a modell architektúrája miatt.

---

**61. Dia: Egyéb torzítások az értékeléseinkben** [cite: 94, 95]

* **Tartalom:** Maguk az értékelési módszerek is lehetnek torzítottak:
    * **Torzított metrikák:** Pl. az n-gram átfedésen alapuló metrikák (BLEU/ROUGE) nem biztos, hogy jól működnek gazdag morfológiájú nyelveknél (pl. magyar, finn), vagy ha a tokenizálás nem egyértelmű[cite: 94].
    * **Torzított LLM-alapú értékelések:** Pl. egy LLM-értékelő preferenciái valószínűleg csak egy szűk (demográfiai) alcsoportot reprezentálnak (pl. a fejlesztőkét vagy a tanítóadatokban domináló csoportét)[cite: 95].
* **Magyarázat:** Felhívja a figyelmet arra, hogy nemcsak a modellek, hanem az általunk használt értékelési eszközök és metrikák is hordozhatnak torzításokat.
    * **Morfológia (Nyelvészet):** A szavak belső szerkezetével, a szóelemek (tövek, képzők, ragok) összekapcsolódásának szabályaival foglalkozó tudományág. A gazdag morfológiájú nyelvekben a szavaknak sokféle alakja lehet, ami kihívást jelenthet a tokenizálás és az n-gram alapú metrikák számára.

---

**62. Dia: Vélemények és értékek: OpinonQA és GlobalOpinionQA** [cite: 96, 97]

* **Tartalom:** Kutatási irány: Annak megértése, hogy az LLM-ek alapértelmezett viselkedése kinek a véleményét tükrözi[cite: 96]. A megközelítés: összehasonlítják az LLM kimeneteinek eloszlását közvélemény-kutatások eredményeivel[cite: 97].
* **Magyarázat:** Vizsgálják, hogy az LLM-ek milyen értékrendet, politikai vagy társadalmi nézeteket képviselnek "alapból", és ezek mennyire egyeznek meg különböző emberi populációk véleményével.

---

**63. Dia: Véleménytorzítások mérése** [cite: 98]

* **Tartalom:** Óvatosnak kell lenni azzal kapcsolatban is, hogy az annotátorok (akik az adatokat címkézik vagy a modelleket értékelik) saját torzításai hogyan szivároghatnak be az LLM-ekbe, különösen az alap (base) nyelvi modellekbe. Hivatkozik a Santurkar et al., 2023, OpinionQA tanulmányra.
* **Magyarázat:** Az emberi annotátorok szubjektivitása és torzításai közvetve befolyásolhatják a modellek viselkedését és "véleményét".

---

**64. Dia: A kihívások kihívásai: Status quo probléma** [cite: 99]

* **Tartalom:** A tudományos kutatóknak érdekükben áll ugyanazokat a (régi) benchmarkokat használni, hogy eredményeiket össze tudják hasonlítani a korábbi munkákkal[cite: 99]. Példa: A gépi fordítási cikkek 82%-a 2019-2020 között még mindig csak a BLEU metrikát használta, annak ellenére, hogy már léteztek olyan metrikák, amelyek jobban korreláltak az emberi ítéletekkel[cite: 99].
* **Magyarázat:** A tudományos publikációs rendszer és az összehasonlíthatóság igénye néha gátolja az újabb, jobb értékelési módszerek elterjedését.

---

**65. Dia: Értékelés: Tanulságok** [cite: 100, 101, 102]

* **Tartalom:** Összefoglaló gondolatok:
    * **Zárt végű feladatok:** Gondolkodj el azon, mit értékelsz (diverzitás, nehézség).
    * **Nyílt végű feladatok:** A tartalmi átfedési metrikák korlátozottan hasznosak (inkább alacsony diverzitású esetekben). A chatbotok értékelése nagyon nehéz, nyitott kutatási probléma a megfelelő példák és értékelési módszerek kiválasztása[cite: 101].
    * **Kihívások:** Légy tisztában a konzisztencia problémáival (jól mérjük-e, amit akarunk?), a kontaminációval (megbízhatunk-e a számokban?), és a különböző torzításokkal.
    * **Végső tanács:** Sok esetben TE vagy a legjobb bírája a kimenet minőségének![cite: 101]. Nézd meg a modell által generált szövegeket, ne csak a számokra hagyatkozz![cite: 102].
* **Magyarázat:** Összegzi az előadás legfontosabb üzeneteit: az értékelés komplex, tele van kihívásokkal, és kritikus gondolkodást igényel. Az automatikus metrikák hasznosak, de korlátozottak, és mindig fontos a generált kimenetek manuális ellenőrzése is.
