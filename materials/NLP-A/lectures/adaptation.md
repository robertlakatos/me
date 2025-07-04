
**Dia 1: Címlap** ([source: 1])

* **Téma:** Természetes Nyelvfeldolgozás Mélytanulással (CS224N/Ling284) - 11. Előadás: Hatékony Adaptáció.
* **Tudnivalók:** Az előadás címe, a kurzus kódja, az előadó neve (Diyi Yang), és a forrásmegjelölés (részben Jesse Mu, Ivan Vulic, Jonas Pfeiffer és Sebastian Ruder anyagai alapján).
* **Megértendő:** Ez az előadás a nagy nyelvi modellek (LLM-ek) új feladatokra való hatékony tanításának módszereiről szól, anélkül, hogy a teljes modellt újra kellene képezni.
* **Elmondandó (Tanárnak):** "Üdvözlöm Önöket a mai előadáson, amely a nagy nyelvi modellek hatékony adaptációjával foglalkozik. Megvizsgáljuk, hogyan tudjuk ezeket a hatalmas modelleket új feladatokra specializálni anélkül, hogy a teljes, költséges újratanítási folyamatot végig kellene vinnünk. Az anyag részben más kutatók munkájára épül, akiket a dián feltüntettünk."

**Dia 2: Áttekintés** ([source: 2])

* **Téma:** Az előadás felépítése és időbeosztása.
* **Tudnivalók:** Az előadás 5 fő részből áll: Prompting (15 perc), Bevezetés a PEFT-be (Parameter-Efficient Fine-Tuning) (10 perc), Pruning/alhálózatok (15 perc), LoRA (15 perc), Adapterek (20 perc). Fontos információ: a 5. házi feladat határideje meghosszabbítva.
* **Megértendő:** Az előadás először bemutatja a legegyszerűbb adaptációs módszert (prompting), majd rátér a paraméter-hatékony finomhangolás (PEFT) koncepciójára és annak három fő megközelítésére.
* **Elmondandó:** "A mai előadás során először megismerkedünk a 'prompting' technikájával, ami egy egyszerű módja a modellek irányításának. Ezután bevezetjük a paraméter-hatékony finomhangolás, röviden PEFT fogalmát, ami kulcsfontosságú a nagy modellek kezelésében. Végül három konkrét PEFT módszert fogunk részletesen megvizsgálni: a ritkítást (pruning), a LoRA-t és az adaptereket. Figyelem, a 5. házi beadási határideje módosult!"

**Dia 3: GPT (2018) - A nagy nyelvi modellek kezdete** ([source: 3])

* **Téma:** Az első Generative Pretrained Transformer (GPT) modell bemutatása.
* **Tudnivalók:** A GPT-1 117 millió paraméterrel rendelkezett ([source: 3]), egy 12 rétegű Transformer dekóderen alapult ([source: 3]), és a BooksCorpus adathalmazon tanították (kb. 4.6 GB szöveg) ([source: 4]). Fontos eredménye, hogy megmutatta, a nagy méretű nyelvi modellezés hatékony előtanítási technika lehet későbbi feladatokhoz, mint pl. a természetes nyelvi következtetés (NLI) ([source: 5]). Példa NLI feladatra ([source: 6]).
* **Megértendő:** A GPT volt az egyik első olyan modell, ami demonstrálta a "pre-training" (előtanítás) és "fine-tuning" (finomhangolás) paradigma erejét: egy általános nyelvi modellen tanult tudást lehet specifikus feladatokra átvinni.
* **Elmondandó:** "Kezdjük az alapoknál. Emlékezzünk vissza az OpenAI GPT modelljére 2018-ból. Ez egy viszonylag 'kicsi' modell volt a maiakhoz képest, 117 millió paraméterrel, de forradalmi volt abban, hogy egy nagy szöveges adathalmazon (könyveken) tanult nyelvi mintázatokat, és ezt a tudást később specifikus feladatokra, mint például a következtetések levonására lehetett használni. Ez az előtanítás alapötlete."

**Dia 4: GPT-2 (2019) - Méretnövekedés** ([source: 7])

* **Téma:** A GPT-2 modell bemutatása.
* **Tudnivalók:** A GPT-2 jelentős méretnövekedést hozott (117M -> 1.5B paraméter), az architektúra alapvetően ugyanaz maradt (Transformer dekóder), de sokkal több adaton tanították (4GB -> 40GB, WebText - Reddit linkek alapján) ([source: 7]). A kapcsolódó publikáció címe: "Language Models are Unsupervised Multitask Learners".
* **Megértendő:** A méret és az adatmennyiség növelése önmagában új képességeket hozott elő a modellben, anélkül, hogy az alapvető architektúrán változtattak volna. A modell "felügyelet nélkül" (unsupervised) tanult meg többféle feladatot ellátni.
* **Elmondandó:** "Egy évvel később jött a GPT-2, ami már tízszer annyi paraméterrel és tízszer annyi adattal rendelkezett. Az alapelv ugyanaz maradt, de ez a méretnövekedés váratlan, úgynevezett 'emergent' (felmerülő) képességeket eredményezett. A modell képessé vált különböző feladatok megoldására anélkül, hogy specifikusan arra tanították volna – innen a cikk címe: 'A nyelvi modellek felügyelet nélküli többcélú tanulók'."

**Dia 5: Emergent Zero-Shot Learning (GPT-2)** ([source: 8])

* **Téma:** A "zero-shot" tanulás képességének megjelenése GPT-2-ben.
* **Tudnivalók:** A zero-shot (nulla példás) tanulás azt jelenti, hogy a modell képes új feladatokat megoldani anélkül, hogy konkrét példákat kapna vagy a súlyait frissítenék (nincs gradiens frissítés) ([source: 8]). Ezt úgy érik el, hogy a feladatot megfelelő szekvencia-jóslási problémaként fogalmazzák meg (pl. kérdés-válasz formátum) ([source: 9]) vagy szekvenciák valószínűségét hasonlítják össze (pl. Winograd séma kihívás) ([source: 10]).
* **Megértendő:** A modell a hatalmas adatmennyiségből tanult általános nyelvi mintázatok alapján képes "kitalálni", hogyan oldjon meg egy új feladatot, pusztán a feladat leírása (prompt) alapján.
* **Elmondandó:** "Az egyik legérdekesebb új képesség a 'zero-shot' tanulás volt. Ez azt jelenti, hogy a GPT-2 képes volt olyan feladatokat megoldani, amikre egyáltalán nem kapott példát a tanítás során. Hogyan? Úgy, hogy a feladatot 'okosan' fogalmazzuk meg neki. Például egy kérdés-válasz feladatnál megadjuk a szövegkörnyezetet, a kérdést, és a modellnek folytatnia kell a szöveget a válasszal. Vagy eldöntheti, melyik mondat a valószínűbb, mint a Winograd példában."

**Dia 6: Zero-Shot Learning Példák (GPT-2)** ([source: 12])

* **Téma:** A zero-shot képességek demonstrálása és a "prompting" bevezetése.
* **Tudnivalók:** A GPT-2 felülmúlta a korábbi csúcsteljesítményt (SoTA) nyelvi modellezési benchmarkokon anélkül, hogy feladatspecifikus finomhangolást kapott volna ([source: 12]). Kreatív feladat-specifikációval érdekes zero-shot viselkedést lehet elérni ([source: 13]), például a CNN/DailyMail összegzési feladatnál a "TL;DR:" (Too Long; Didn't Read) prompt használatával ([source: 14]). Ez a technika a "prompting" ([source: 15]).
* **Megértendő:** A prompt (a modellnek adott instrukció vagy kontextus) megfogalmazása kulcsfontosságú a zero-shot teljesítményhez. A "TL;DR:" egy korai példa a prompt engineeringre.
* **Elmondandó:** "Láthatjuk, hogy a GPT-2 már finomhangolás nélkül is kiváló eredményeket ért el. Sőt, ha ügyesen fogalmazzuk meg a 'kérést' – amit promptnak nevezünk –, akkor meglepő dolgokra képes. Például ha egy hosszú cikk végére odaírjuk, hogy 'TL;DR:', a modell megpróbálja összefoglalni azt. Ez a 'prompting', a modell irányítása a bemeneti szövegen keresztül."

**Dia 7: GPT-3 (2020) - Újabb ugrás** ([source: 16])

* **Téma:** A GPT-3 modell bemutatása.
* **Tudnivalók:** Újabb jelentős növekedés mind méretben (1.5B -> 175B paraméter), mind adatmennyiségben (40GB -> 600+ GB) ([source: 16]). A kapcsolódó publikáció címe: "Language Models are Few-Shot Learners".
* **Megértendő:** A skálázás (méret és adat növelése) továbbra is kulcsfontosságú, és újabb emergent képességeket hoz elő.
* **Elmondandó:** "A következő nagy lépés a GPT-3 volt 2020-ban. Ismét drasztikus növekedés: több mint százszorosára nőtt a paraméterek száma (175 milliárd!) és az adatmennyiség is. Ahogy a cím is sugallja – 'A nyelvi modellek kevés példából tanulók' –, itt egy újabb képesség került előtérbe."

**Dia 8: Emergent Few-Shot Learning (GPT-3)** ([source: 17])

* **Téma:** A "few-shot" (kevés példás) tanulás képességének megjelenése GPT-3-ban.
* **Tudnivalók:** A few-shot tanulás (más néven in-context learning) azt jelenti, hogy a feladatot úgy specifikáljuk, hogy a promptba néhány példát is beillesztünk a megoldandó példa elé ([source: 17]). Fontos, hogy eközben sem történik gradiens frissítés (a modell súlyai nem változnak) ([source: 17]). Példák: szavak betűinek helyrerakása, fordítás.
* **Megértendő:* A modell képes a promptban látott néhány példa alapján "ráérezni" a feladatra és alkalmazni a mintát az új bemenetre. Ez hatékonyabb lehet, mint a zero-shot, de még mindig nem igényel modellfrissítést.
* **Elmondandó:** "A GPT-3 megmutatta, hogy nem csak nulla, de néhány példa alapján is képes tanulni ('few-shot learning' vagy 'in-context learning'). Egyszerűen a prompt elejére biggyesztünk 1-2-5 példát a feladatról és a megoldásról, majd megadjuk az új problémát. A modell a kontextusból, a példákból próbálja megérteni a feladatot, anélkül, hogy a belső súlyait módosítaná. Nézzünk pár példát, mint a szókirakó vagy a fordítás."

**Dia 9: Few-Shot Teljesítmény (Zero-Shot)** ([source: 18])

* **Téma:** GPT-3 teljesítménye nulla példával (K=0) a SuperGLUE benchmarkon.
* **Tudnivalók:** Az ábra mutatja a GPT-3 (175B) teljesítményét különböző számú példa (K) esetén a SuperGLUE feladatgyűjteményen, összehasonlítva finomhangolt modellekkel (BERT Large, BERT++, SOTA) és az emberi teljesítménnyel. A K=0 oszlop a zero-shot esetet mutatja. Példa: Angol-francia fordítás (zero-shot).
* **Megértendő:** A zero-shot GPT-3 már önmagában is jelentős teljesítményre képes, bár elmarad a finomhangolt modellektől és az emberektől.
* **Elmondandó:** "Ez a grafikon a SuperGLUE nevű komplex nyelvértési tesztcsaládon mutatja a GPT-3 teljesítményét. A vízszintes tengelyen az látható, hány példát (K) adtunk a modellnek a promptban. Az első oszlop (K=0) a zero-shot eset. Látható, hogy a 175 milliárd paraméteres GPT-3 már nulla példával is messze a véletlen találgatás felett teljesít, de még elmarad a speciálisan finomhangolt modellektől."

**Dia 10: Few-Shot Teljesítmény (One-Shot)** ([source: 19])

* **Téma:** GPT-3 teljesítménye egy példával (K=1) a SuperGLUE benchmarkon.
* **Tudnivalók:** Az ábra ugyanaz, mint az előző, de most a K=1 esetre fókuszálunk. Példa: Angol-francia fordítás (one-shot).
* **Megértendő:** Egyetlen példa hozzáadása a promptban már javíthat a teljesítményen.
* **Elmondandó:** "Ha csak egyetlen példát adunk (K=1, 'one-shot' tanulás), a teljesítmény általában javul. Látjuk a grafikonon is a növekvő tendenciát. Például a fordításnál megadjuk: 'sea otter => loutre de mer', majd kérdezzük: 'cheese => ?'."

**Dia 11: Few-Shot Teljesítmény (Few-Shot)** ([source: 20])

* **Téma:** GPT-3 teljesítménye több példával (K>1) a SuperGLUE benchmarkon.
* **Tudnivalók:** Az ábra mutatja a teljesítmény növekedését több példa (few-shot) esetén.
* **Megértendő:** Több példa (egy bizonyos pontig) általában jobb teljesítményt eredményez az in-context learning során. A GPT-3 few-shot képességeivel már megközelíti vagy akár meg is haladja a finomhangolt modellek teljesítményét bizonyos feladatokon.
* **Elmondandó:** "Ahogy növeljük a példák számát (K=4, 8, 16, 32 – 'few-shot' tanulás), a GPT-3 teljesítménye tovább javul, és egyre közelebb kerül a speciálisan finomhangolt modellek, sőt néha az emberi szinthez is. Ez mutatja a skála és a kevés példából való tanulás erejét."

**Dia 12: Few-Shot mint Emergent Tulajdonság** ([source: 21])

* **Téma:** A few-shot tanulás képessége a modell méretével (skálájával) együtt jelenik meg.
* **Tudnivalók:** Az ábra szintetikus "szókirakó" feladatokon mutatja, hogy a few-shot (itt 100-shot) tanulási képesség drámaian javul a modell méretének növekedésével. Kisebb modelleknél alig működik, míg a legnagyobb modelleknél nagyon hatékony ([source: 21]).
* **Megértendő:** A few-shot tanulás nem egyszerűen a több adat eredménye, hanem a modell komplexitásának (méretének) növekedésével együtt "felbukkanó" (emergent) tulajdonság.
* **Elmondandó:** "Fontos megérteni, hogy ez a few-shot tanulási képesség nem volt jelen a kisebb modelleknél. Ez egy 'emergent' tulajdonság, ami csak egy bizonyos modellméret felett jelenik meg igazán erőteljesen. Minél nagyobb a modell, annál jobban képes általánosítani a promptban látott néhány példából."

**Dia 13: Prompting vs. Finomhangolás** ([source: 22])

* **Téma:** A két fő paradigma vizuális összehasonlítása.
* **Tudnivalók:** A hagyományos finomhangolás során a teljes előtanított modell súlyait frissítik a célfeladat adatai alapján. A zero/few-shot prompting során az előtanított modell súlyai változatlanok maradnak, és a feladatot a bemeneti prompt segítségével specifikálják ([source: 22]).
* **Megértendő:** Két alapvetően eltérő megközelítés a modellek adaptálására: az egyik a modell belső paramétereit módosítja, a másik a bemeneten keresztül irányítja a fix modellt.
* **Elmondandó:** "Tehát két fő utat látunk a modellek új feladatokra való használatára. A 'régi' módszer a finomhangolás: fogjuk az előtanított modellt, és a célfeladat adatain tovább tanítjuk, frissítve az összes súlyát. Az újabb, a GPT-3 által népszerűsített módszer a prompting: az eredeti modellhez nem nyúlunk, csak a bemeneti promptot fogalmazzuk meg ügyesen, esetleg néhány példával, hogy rávezessük a megoldásra."

**Dia 14: A Prompting korlátai** ([source: 23])

* **Téma:** Olyan feladatok, ahol a prompting önmagában nem elég hatékony.
* **Tudnivalók:** Vannak feladatok, különösen amelyek összetettebb, többlépéses gondolkodást igényelnek, amelyeket még a nagy modellek sem tudnak jól megoldani pusztán promptinggal ([source: 24]). Példa: többjegyű számok összeadása ([source: 25]). A megoldás lehet a prompt megváltoztatása ([source: 25]).
* **Megértendő:** Az egyszerű prompting nem csodaszer, komplexebb logikai vagy matematikai feladatoknál gyakran hibázik.
* **Elmondandó:** "Bár a prompting lenyűgöző, megvannak a korlátai. Olyan feladatoknál, amik precíz, lépésről-lépésre történő gondolkodást igényelnek, mint például ez a többjegyű összeadás, a modellek gyakran hibáznak, ha csak a végeredményt kérjük tőlük. Mit tehetünk ilyenkor? Meg kell próbálnunk 'jobb' promptot adni."

**Dia 15: Chain-of-Thought (CoT) Prompting** ([source: 26])

* **Téma:** A "gondolatmenet" (Chain-of-Thought) prompting bemutatása.
* **Tudnivalók:** A CoT prompting lényege, hogy a promptban nemcsak a végeredményt adjuk meg a példákban, hanem a megoldáshoz vezető gondolatmenetet, lépéseket is ([source: 26]). Ez segít a modellnek a komplexebb feladatok megoldásában. A példában a többjegyű összeadásnál bemutatják a lépésenkénti számolást.
* **Megértendő:** Ha a modellt rávezetjük, hogy "gondolkodjon hangosan", lépésről lépésre vezesse le a megoldást, akkor sokkal jobb eredményeket érhet el komplexebb feladatoknál.
* **Elmondandó:** "Egy hatékony technika a 'Chain-of-Thought' vagy 'gondolatmenet' prompting. Ahelyett, hogy csak a végeredményt mutatnánk meg a példákban, leírjuk a megoldáshoz vezető logikai lépéseket is. Ahogy itt az összeadásnál látjuk, a részeredmények levezetése segít a modellnek a helyes végeredmény elérésében. Lényegében arra kérjük, hogy 'gondolkodjon lépésről lépésre'."

**Dia 16: CoT mint Emergent Tulajdonság** ([source: 27])

* **Téma:** A CoT prompting hatékonysága is a modell méretével nő.
* **Tudnivalók:** Az ábra (középiskolás szöveges matematikai feladatokon) mutatja, hogy a CoT prompting (a zöld vonal) hatékonysága drámaian megnő a modell méretének növekedésével, míg a standard prompting (kék vonal) kevésbé skálázódik ezen a feladattípuson ([source: 27], [source: 28]).
* **Megértendő:** Has*onlóan a few-shot tanuláshoz, a CoT prompting igazi ereje is csak a kellően nagy modelleknél mutatkozik meg.
* **Elmondandó:** "És ahogy a few-shot tanulásnál láttuk, a Chain-of-Thought prompting hatékonysága is egy 'emergent' tulajdonság. Kisebb modelleknél nem sokat segít, de ahogy növeljük a modell méretét, a CoT drámaian javítja a teljesítményt, különösen a gondolkodást igénylő feladatokon, mint a szöveges matek példák."

**Dia 17: Zero-Shot CoT - Kérdés** ([source: 29])

* **Téma:** Felvetődik a kérdés: szükség van-e egyáltalán gondolkodási példákra?
* **Tudnivalók:** Az előző CoT példa few-shot volt (mutattunk lépésről-lépésre megoldott példákat). Felmerül a kérdés: Működik-e a CoT akkor is, ha nem adunk példákat, csak egyszerűen megkérjük a modellt, hogy gondolkodjon lépésről lépésre? ([source: 30]).
* **Megértendő:** Lehetséges, hogy a modellt explicit példák nélkül is rá lehet venni a lépésenkénti gondolkodásra?
* **Elmondandó:** "Az előbb láttunk egy 'few-shot' CoT példát, ahol megmutattuk a gondolatmenetet. De vajon muszáj ez? Mi lenne, ha egyszerűen csak megkérnénk a modellt: 'Gondolkodjunk lépésről lépésre', anélkül, hogy konkrét példát mutatnánk a lépésekre?"

**Dia 18: Zero-Shot CoT Példa** ([source: 33])

* **Téma:** A Zero-Shot CoT demonstrálása.
* **Tudnivalók:** A példa egy zsonglőrös feladat ([source: 34], [source: 35]). Ahelyett, hogy megoldási példákat adnánk, egyszerűen hozzáadjuk a "Let’s think step by step." (Gondolkodjunk lépésről lépésre.) instrukciót a kérdés után ([source: 33]). A modell ezután maga generálja a gondolatmenetet ([source: 31], [source: 32]) a végső válasz előtt.
* **Megértendő:** Egy egyszerű instrukció hozzáadása elegendő lehet ahhoz, hogy a modell aktiválja a lépésenkénti gondolkodási képességét.
* **Elmondandó:** "És a válasz igen! Működik a 'Zero-Shot CoT'. Nézzük ezt a példát: feltesszük a kérdést a labdákról, és a végére csak annyit írunk: 'Gondolkodjunk lépésről lépésre.' ([source: 33]). A modell erre magától elkezdi levezetni a megoldást: összesen 16 labda van ([source: 31]), fele golflabda, az 8 ([source: 31]). A golflabdák fele kék, az 4 ([source: 32]). Tehát 4 kék golflabda van. Mindezt anélkül, hogy mutattunk volna neki hasonló levezetést!"

**Dia 19: Zero-Shot CoT Teljesítmény** ([source: 36])

* **Téma:** A Zero-Shot CoT összehasonlítása más módszerekkel.
* **Tudnivalók:** Az ábra mutatja, hogy a Zero-Shot CoT (lila oszlop) jelentősen felülmúlja a standard Zero-Shot promptingot (kék oszlop) ([source: 36]). Azonban a manuálisan megírt gondolatmenetet tartalmazó Few-Shot CoT (zöld oszlop, "Manual CoT") általában még ennél is jobb eredményt ad ([source: 36]).
* **Megértendő:** A Zero-Shot CoT egy egyszerű, de hatékony javítás a standard zero-shothoz képest, de a gondosan megírt few-shot példák még többet segíthetnek.
* **Elmondandó:** "Összehasonlítva a teljesítményt: a Zero-Shot CoT (csak az instrukció hozzáadásával) sokkal jobb, mint a sima zero-shot prompting. Azonban, ha adunk a modellnek néhány, általunk gondosan kidolgozott, lépésről-lépésre levezetett példát (Manual CoT), azzal általában még jobb eredményt érhetünk el. Tehát a 'Gondolkodj lépésről lépésre!' egy jó kiindulópont, de a few-shot CoT lehet még erősebb."

**Dia 20: Haladó Prompting Technikák** ([source: 37])

* **Téma:** További fejlett prompting módszerek említése.
* **Tudnivalók:** Léteznek még komplexebb prompting stratégiák, mint például amikor a nyelvi modell maga tervezi meg a promptot vagy a gondolatmenetet (pl. Auto-CoT, LM-Designed CoT) ([source: 37]). Ezek tovább javíthatják az eredményeket.
* **Megértendő:** A prompting egy aktívan kutatott terület, folyamatosan jelennek meg új, kifinomultabb technikák.
* **Elmondandó:** "A kutatás nem állt meg a Zero-Shot CoT-nál. Vannak még ennél is kifinomultabb technikák, például olyanok, ahol maga a nyelvi modell segít a legjobb prompt vagy gondolatmenet megtervezésében. Ezekkel még tovább lehet növelni a pontosságot."

**Dia 21: Prompt Engineering Művészete** ([source: 38])

* **Téma:** A "prompt engineering" mint új szakma/készség.
* **Tudnivalók:** A hatékony promptok megalkotása ("prompt engineering") egyre fontosabbá válik ([source: 38]). Ez magában foglalhatja speciális formázási kéréseket (pl. Google kódfejléc) ([source: 38]), a gondolkodás explicit kérését ([source: 39]), de árnyoldalai is vannak, mint a modellekben rejlő torzítások (bias) és toxicitás felerősítése ([source: 40]), vagy a modellek biztonsági korlátainak kijátszása ("jailbreaking") ([source: 40]).
* **Megértendő:** A promptolás nem csak technika, hanem már-már művészet, amihez kreativitás, kísérletezés és a modell működésének mélyebb megértése szükséges, beleértve a potenciális veszélyeket is.
* **Elmondandó:** "Mindezek alapján láthatjuk, hogy a jó prompt megírása lassan külön szakmává, 'prompt engineeringgé' válik. Ez nem csak annyi, hogy felteszünk egy kérdést. Tudnunk kell, hogyan kérjünk specifikus formátumot, hogyan bírjuk rá a modellt a gondolkodásra, de tisztában kell lennünk a veszélyekkel is: a rossz prompt felerősítheti a modell torzításait, vagy akár a biztonsági korlátok kijátszására is használható."

**Dia 22: Prompt Engineering (Vizuális)** ([source: 41])

* **Téma:** Vizuális illusztráció vagy mém a prompt engineeringről.
* **Tudnivalók:** Valószínűleg egy kép vagy ábra, ami szemlélteti a prompt engineering komplexitását vagy humoros oldalát.
* **Megértendő:** A prompt engineering lehet bonyolult és néha frusztráló folyamat.
* **Elmondandó:** "Ez az ábra/kép jól illusztrálja, hogy a prompt engineering néha milyen összetett tud lenni..." (Az aktuális kép alapján kell magyarázni.)

**Dia 23: A Prompt-alapú tanulás hátrányai** ([source: 42])

* **Téma:** A prompting módszer korlátai és problémái.
* **Tudnivalók:**
    1.  **Ineffektivitás:** A teljes promptot minden egyes predikciónál újra fel kell dolgozni ([source: 42]).
    2.  **Gyengébb teljesítmény:** Általában rosszabbul teljesít, mint a finomhangolás ([source: 43]).
    3.  **Érzékenység:** Nagyon érzékeny a prompt megfogalmazására ([source: 44]), a példák sorrendjére ([source: 45]) stb.
    4.  **Nehéz értelmezhetőség:** Nem világos, mit tanul meg a modell a promptból (még véletlenszerű címkékkel is működhet!) ([source: 46]).
* **Megértendő:** A prompting gyors és nem igényel modellfrissítést, de számítási és teljesítménybeli hátrányai vannak, és a működése néha kiszámíthatatlan.
* **Elmondandó:** "Bár a prompting rugalmas, vannak hátrányai is. Először is, minden alkalommal, amikor használjuk a modellt, az egész hosszú promptot (példákkal, instrukciókkal együtt) újra kell értelmeznie, ami lassú lehet. Másodszor, a tapasztalatok szerint a finomhangolással általában jobb pontosság érhető el. Harmadszor, nagyon érzékeny arra, hogyan fogalmazunk, milyen sorrendben adjuk a példákat – egy kis változtatás is nagy különbséget okozhat. Végül pedig nehéz megmondani, mit 'tanul' a modell a promptból, néha egészen meglepő dolgok is működnek, ami a megbízhatóságot kérdőjelezi meg."

**Dia 24: Bevezetés a Paraméter-Hatékony Finomhangolásba (PEFT)** ([source: 47])

* **Téma:** A PEFT koncepciójának bevezetése, szembeállítva a teljes finomhangolással.
* **Tudnivalók:** A **Teljes Finomhangolás (Full Fine-tuning)** során a modell összes paraméterét frissítik. A **Paraméter-Hatékony Finomhangolás (PEFT)** során csak a paraméterek egy kis részhalmazát frissítik ([source: 47]). Miért van erre szükség? 1. A teljes finomhangolás kivitelezhetetlen a hatalmas modelleknél (pl. GPT-3). 2. A modern modellek masszívan túlparaméterezettek. 3. A PEFT módszerekkel a teljes finomhangoláshoz hasonló teljesítmény érhető el ([source: 48]).
* **Megértendő:** A PEFT egy kompromisszum: a teljes finomhangolás pontosságát célozza meg, de sokkal kevesebb számítási és tárolási erőforrás felhasználásával, azáltal, hogy csak a modell egy kis részét módosítja.
* **Elmondandó:** "Mivel a promptingnak vannak korlátai, és a teljes finomhangolás a milliárdos paraméterű modelleknél már szinte lehetetlen (gondoljunk a szükséges GPU memóriára és időre), szükség van egy köztes megoldásra. Ez a Paraméter-Hatékony Finomhangolás, vagy PEFT. Az alapötlet az, hogy nem az egész modellt hangoljuk, csak egy kis részét. Miért működhet ez? Egyrészt, mert ezek a modellek annyira nagyok, hogy rengeteg a 'felesleges' paraméterük, másrészt a tapasztalat az, hogy a PEFT módszerekkel közel olyan jó eredményt lehet elérni, mint a teljes finomhangolással, de töredék erőforrásból."

**Dia 25: Miért van szükség hatékony adaptációra?** ([source: 49])

* **Téma:** A PEFT szükségességének tágabb kontextusa.
* **Tudnivalók:**
    1.  **AI paradigma:** Jelenleg a pontosságot helyezik előtérbe a hatékonysággal szemben ([source: 49], [source: 50]).
    2.  **Környezeti költségek:** Az LLM-ek tanításának (és finomhangolásának) rejtett környezeti terhei vannak (energiafogyasztás) ([source: 49]).
    3.  **Koncentráció:** A magas tanítási költségek miatt az AI fejlesztés a nagy, jól finanszírozott (ipari) szervezetekben összpontosul ([source: 49]).
* **Megértendő:** A hatékonyság nemcsak technikai, hanem környezeti és társadalmi kérdés is az AI területén. A PEFT hozzájárulhat a fenntarthatóbb és demokratikusabb AI fejlesztéshez.
* **Elmondandó:** "De miért olyan fontos ez a hatékonyság? Egyrészt, a jelenlegi AI kutatás gyakran a pontosság maximalizálására fókuszál, figyelmen kívül hagyva a hatékonysági szempontokat. Másrészt, ezeknek a modelleknek a tanítása és futtatása óriási energiafogyasztással jár, aminek komoly környezeti lábnyoma van. Harmadrészt, a gigantikus költségek miatt a legmodernebb AI fejlesztés néhány nagy ipari szereplő kezében összpontosul, ami korlátozza a hozzáférést és az innovációt. A PEFT ezen problémák enyhítésében segíthet." (Hivatkozás: Green AI koncepció)

**Dia 26: Mennyi energiába kerül egy nyelvi modell tanítása?** ([source: 51])

* **Téma:** Konkrét példák a modellek energiaigényére.
* **Tudnivalók:** Az ábra (Strubell et al., 2019 alapján [source: 52]) bemutatja különböző NLP modellek (pl. Transformer, BERT, GPT-3) tanításának becsült szén-dioxid-kibocsátását és energiafogyasztását, összehasonlítva hétköznapi dolgokkal (pl. autó élettartama, emberi élet, USA-NY repülőút).
* **Megértendő:** A nagy modellek tanítása rendkívül energiaigényes, ami jelentős környezeti terhelést jelent.
* **Elmondandó:** "Hogy érzékeltessük a mértékeket: ez az ábra megmutatja, hogy egy-egy nagyobb modell tanítása mennyi energiát fogyaszt és mekkora szén-dioxid-kibocsátással jár. Láthatjuk, hogy egy komplexebb modell tanítása több energiát igényelhet, mint egy autó teljes élettartama alatt, vagy egy transzatlanti repülőút. Ezért kulcsfontosságú a hatékonyabb módszerek keresése."

**Dia 27: Egy egyetemi kurzus hatása** ([source: 54])

* **Téma:** Relatív kis léptékű feladatok energiaigénye.
* **Tudnivalók:** Egy stanfordi példa (CS234 kurzus): ha a diákok egy házi feladatban a kevésbé energiahatékony algoritmust használták, az jelentős többletfogyasztást okozott. A hatékonyabb algoritmus választásával kb. egy átlagos amerikai háztartás havi fogyasztásának megfelelő energiát takaríthattak volna meg ([source: 54], [source: 55]).
* **Megértendő:** Még a kisebb léptékű AI feladatoknál és a tanulás során is számít az energiahatékonyság.
* **Elmondandó:** "És ez nem csak az ipari méretű modellekre igaz. Ez a példa egy stanfordi kurzusról azt mutatja, hogy még egy egyetemi házi feladat során is jelentős energiát lehet megtakarítani, ha a diákok a hatékonyabb algoritmust választják. Ez rávilágít arra, hogy a hatékonyságra való törekvés mindannyiunk felelőssége."

**Dia 28: Az AI fejlesztés koncentrációja** ([source: 57])

* **Téma:** Miért összpontosul a fejlesztés kevés szervezetnél?
* **Tudnivalók:** Az okok: szükség van hatalmas tanítási adathalmazokra ([source: 58]), óriási számítási kapacitásra ([source: 58]), és a modellek telepítéséhez/üzemeltetéséhez szükséges infrastruktúrára ([source: 58]). Az ábra a generatív AI modellek kiadásának módszereit és megfontolásait mutatja.
* **Megértendő:** A magas erőforrásigény korlátozza, hogy kik tudnak részt venni a legmodernebb AI fejlesztésben.
* **Elmondandó:** "Ahogy említettük, a legfejlettebb AI modellek fejlesztése egyre inkább a nagy technológiai cégeknél és kutatóintézeteknél összpontosul. Ennek oka egyszerűen az, hogy nekik van hozzáférésük a szükséges óriási adatmennyiséghez, a szuperszámítógépes kapacitáshoz és a telepítési infrastruktúrához. Ez felveti a hozzáférhetőség és a fejlesztés demokratizálásának kérdését."

**Dia 29: A PEFT különböző nézőpontjai** ([source: 59])

* **Téma:** A PEFT módszerek osztályozásának három szempontja.
* **Tudnivalók:** A PEFT módszereket három fő nézőpontból közelíthetjük meg:
    1.  **Paraméter nézőpont:** Mely paramétereket módosítjuk?
    2.  **Bemenet nézőpont:** Hogyan módosítjuk a modell bemenetét?
    3.  **Funkció nézőpont:** Hogyan módosítjuk vagy egészítjük ki a modell funkcióit?
    (Forrás: EMNLP 2022 Tutorial [source: 59], [source: 60])
* **Megértendő:** Ez a három nézőpont segít rendszerezni és megérteni a különböző PEFT technikák alapelvét.
* **Elmondandó:** "Most, hogy láttuk a PEFT fontosságát, nézzük meg, hogyan lehet ezeket a módszereket csoportosítani. Három fő nézőpontot különböztetünk meg, attól függően, hogy hol avatkozunk be a modell működésébe: a paraméterek szintjén, a bemenet szintjén, vagy a modell belső funkcióinak szintjén. Az elkövetkezőkben ezeket vesszük sorra."

**Dia 30: Paraméter Perspektíva - Áttekintés** ([source: 61])

* **Téma:** A paraméter-alapú PEFT módszerek két fő típusa.
* **Tudnivalók:** Ebbe a kategóriába tartozik:
    1.  Ritka Alhálózatok (Sparse Subnetworks) - pl. Pruning (Ritkítás)
    2.  Alacsony Rangú Kompozíció (Low-rank Composition) - pl. LoRA
* **Megértendő:** Két fő stratégia van a paraméterek hatékony módosítására: vagy csak egy kis, ritka részhalmazt tartunk meg/módosítunk, vagy a módosításokat egy alacsonyabb dimenziós térben reprezentáljuk.
* **Elmondandó:** "A paraméter nézőponton belül két fő irányzatot különböztetünk meg. Az egyik a 'ritkítás', ahol a modell eredeti paramétereinek nagy részét 'eldobjuk' vagy 'lefagyasztjuk', és csak egy kis alhálózattal dolgozunk. A másik az 'alacsony rangú kompozíció', ahol a szükséges változtatásokat egy sokkal kisebb, tömörített formában reprezentáljuk. Kezdjük a ritkítással."

**Dia 31: Ritka Alhálózatok (Pruning)** ([source: 62])

* **Téma:** A pruning (ritkítás) alapötlete.
* **Tudnivalók:** Gyakori induktív előfeszítés a modul paramétereire a ritkaság ([source: 62]). A leggyakoribb módszer a pruning (ritkítás). Ez felfogható egy bináris maszk (M ∈ {0, 1}^d) alkalmazásaként, ami szelektíven megtartja vagy eltávolítja a kapcsolatokat, létrehozva egy alhálózatot ([source: 63]). Gyakori kritérium a súlyok nagysága (magnitude) ([source: 64]).
* **Megértendő:** A pruning során a modell kapcsolatainak (súlyainak) egy részét nullává tesszük, így egy kisebb, "ritkább" modellt kapunk. Gyakran a kis abszolút értékű súlyokat távolítjuk el.
* **Elmondandó:** "A legegyszerűbb módja egy modell 'kicsinyítésének' a ritkítás, vagy angolul 'pruning'. Az ötlet az, hogy a neurális hálózatban lévő kapcsolatok (súlyok) közül sokat feleslegesnek tekintünk. A pruning során ezeket a 'felesleges' kapcsolatokat egyszerűen eltávolítjuk, azaz a súlyukat nullára állítjuk. Ezt úgy képzelhetjük el, mintha egy maszkot tennénk a hálózatra, ami csak a fontos kapcsolatokat engedi át. A legegyszerűbb módszer a legkisebb abszolút értékű súlyok eltávolítása."

**Dia 32: A Pruning Folyamata** ([source: 65])

* **Téma:** A pruning lépései.
* **Tudnivalók:** A folyamat:
    1.  **Kezdeti tanítás:** A teljes modellt betanítjuk (vagy egy előtanított modellt használunk).
    2.  **Pruning:** A legkisebb magnitúdójú súlyok egy részét eltávolítjuk (nullázzuk) ([source: 65]).
    3.  **Újratanítás:** A megmaradt (nem nullázott) súlyokat tovább tanítjuk a célfeladaton ([source: 65]).
    Ez lehet **egylépéses (one-shot)** vagy **iteratív** (több pruning-újratanítás ciklus) ([source: 65]).
* **Megértendő:** A pruning nem csak a súlyok eldobásából áll; fontos lépés a megmaradt súlyok finomhangolása (újratanítása), hogy kompenzálják az eltávolítottakat. Az iteratív megközelítés gyakran jobb eredményt ad.
* **Elmondandó:** "A pruning általában nem egyetlen lépés. Először betanítjuk a sűrű modellt, majd 'lenyessük' a legkisebb súlyokat. Ezután a megmaradt, 'megritkított' modellt újra finomhangoljuk, hogy a megmaradt súlyok átvehessék az eltávolítottak szerepét. Ezt a folyamatot (nyesés -> újratanítás) többször is megismételhetjük, ezt nevezzük iteratív pruningnak, ami gyakran hatékonyabb, mint az egylépéses."

**Dia 33: Pruning mint Maszkolás / Delta** ([source: 66])

* **Téma:** A pruning alternatív értelmezései.
* **Tudnivalók:**
    * Felfogható úgy, mint egy feladatspecifikus vektor (Δθ) hozzáadása az eredeti paraméterekhez (θ₀), ahol a nullázott súlyokra Δθ = -θ₀ ([source: 66], [source: 67]).
    * Vagy: az eredeti súlyok (θ₀) szorzása egy bináris maszkkal (M): θ_sparse = θ₀ ∘ M ([source: 67]).
    * **Diff pruning:** Csak a finomhangolás során bekövetkezett változás (Δθ) nagysága alapján végzünk ritkítást, nem a végső súlyok (θ₀ + Δθ) nagysága alapján ([source: 68]).
* **Megértendő:** A pruning matematikailag többféleképpen is leírható, ami segíthet a különböző variánsok megértésében. A Diff pruning arra fókuszál, hogy mely súlyok változtak *sokat* a finomhangolás során.
* **Elmondandó:** "A pruningra gondolhatunk úgy is, mint egy speciális 'delta' (változás) hozzáadására az eredeti súlyokhoz, ahol a törölt súlyok deltája pont az eredeti súly negáltja. Vagy egyszerűbben, mint az eredeti súlymátrix megszorzása egy bináris maszkkal. Egy érdekes változat a 'Diff pruning', ahol nem a súlyok végső értékét nézzük, hanem azt, hogy mennyit változtak a finomhangolás alatt – azokat a súlyokat tartjuk meg, amik a legtöbbet 'mozdultak'."

**Dia 34: A Lottószelvény Hipotézis (Lottery Ticket Hypothesis)** ([source: 69])

* **Téma:** Léteznek-e eleve "nyerő" alhálózatok a sűrű modellekben?
* **Tudnivalók:** A hipotézis szerint a sűrű, véletlenszerűen inicializált (vagy előtanított) modellek tartalmaznak olyan ritka alhálózatokat ("nyerő szelvények"), amelyek izoláltan tanítva képesek elérni az eredeti sűrű hálózat teljesítményét, hasonló számú iteráció alatt ([source: 69]). Ezt igazolták NLP modellekre (pl. BERT) is ([source: 70]). A szükséges ritkaság (sparsity ratio) feladattól függően 40-90% is lehet ([source: 70]). Az általános feladaton (pl. maszkolt nyelvi modellezés) tanított alhálózatok jól transzferálhatók ([source: 70]).
* **Megértendő:** Lehet, hogy a nagy modellek eleve tartalmaznak kicsi, de hatékony alhálózatokat, és a tanítás/pruning feladata ezek megtalálása.
* **Elmondandó:** "Egy izgalmas elmélet a 'Lottószelvény Hipotézis'. Eszerint a nagy, sűrű hálózatok tele vannak 'rejtett' kis, ritka alhálózatokkal, amik önmagukban is képesek lennének megoldani a feladatot, ha megtalálnánk őket – ezek a 'nyerő lottószelvények'. A tanítás és a pruning egyik célja eszerint ezeknek a nyerő alhálózatoknak a felderítése. A BERT-re például kimutatták, hogy akár a súlyok 90%-át is el lehet távolítani bizonyos feladatoknál anélkül, hogy a pontosság jelentősen csökkenne, ha a megfelelő alhálózatot találjuk meg."

**Dia 35: Előtanított Modellek Pruningja (Movement Pruning)** ([source: 71])

* **Téma:** Specifikus pruning stratégia előtanított modellek finomhangolásához.
* **Tudnivalók:** A finomhangolás során a súlyok általában közel maradnak az előtanított értékükhöz ([source: 71]). A **Magnitude pruning** (nagyság alapú) azokat a súlyokat tartja meg, amik messze vannak a nullától (eleve nagyok voltak) ([source: 72]). A **Movement pruning** (mozgás alapú) azokat tartja meg, amelyek a finomhangolás során a *legjobban eltávolodtak* a nullától (azaz a legtöbbet változtak) ([source: 71], [source: 72]).
* **Megértendő:** Amikor egy előtanított modellt finomhangolunk, nem feltétlenül az eredetileg legnagyobb súlyok a legfontosabbak az új feladathoz, hanem azok, amelyek a finomhangolás során jelentősen módosultak.
* **Elmondandó:** "Ha egy már előtanított modellt finomhangolunk, a legtöbb súly nem változik drasztikusan. A hagyományos magnitúdó alapú pruning azokat a súlyokat tartaná meg, amik eleve nagyok voltak. De lehet, hogy az új feladathoz pont azok a súlyok a fontosak, amik a finomhangolás során *sokat változtak*, még ha nem is lettek feltétlenül a legnagyobbak. Erre épít a 'Movement pruning': azokat a súlyokat tartja meg, amik a legjobban 'elmozdultak' a nullától a finomhangolás során."

**Dia 36: Paraméter Perspektíva - Összegzés + Következő** ([source: 73])

* **Téma:** A ritka alhálózatok lezárása, áttérés az alacsony rangú kompozícióra.
* **Tudnivalók:** Összegzés: A ritka alhálózatok (pruning) az egyik módja a paraméter-hatékony adaptációnak. Következő téma: Alacsony Rangú Kompozíció (Low-rank Composition).
* **Megértendő:** Láttuk az egyik fő paraméter-hatékony stratégiát, most jön a másik.
* **Elmondandó:** "Tehát a ritkítás (pruning) és a lottószelvény hipotézis az egyik megközelítés a paraméterek számának csökkentésére. Most nézzük meg a másik fő irányt a paraméter perspektíván belül: az alacsony rangú kompozíciót, aminek legismertebb példája a LoRA."

**Dia 37: Teljes Finomhangolás Újra (Formálisan)** ([source: 74])

* **Téma:** A teljes finomhangolás matematikai leírása.
* **Tudnivalók:** Adott egy előtanított modell (pl. GPT) paraméterekkel (θ₀), ami a P_θ₀(y|x) eloszlást modellezi ([source: 74]). Cél: adaptálni egy downstream feladatra (pl. összegzés) egy (xᵢ, yᵢ) párokból álló tanító adathalmaz segítségével. Teljes finomhangolás: θ₀ -> θ₀ + Δθ frissítés a célfüggvény (pl. feltételes log-likelihood) maximalizálásával ([source: 75]).
* **Megértendő:** A teljes finomhangolás során az összes eredeti paraméter (θ₀) módosulhat (Δθ), hogy maximalizálja a modell teljesítményét az új adatokon.
* **Elmondandó:** "Mielőtt belevágnánk a LoRA-ba, idézzük fel formálisan, mit is jelent a teljes finomhangolás. Van egy előtanított modellünk, θ₀ paraméterekkel. Kapunk egy új adathalmazt a célfeladathoz. A teljes finomhangolás során az összes paramétert módosítjuk (ezt a változást jelöljük Δθ-val), hogy a modell a lehető legjobban teljesítsen az új adatokon, általában a valószínűségi célfüggvény maximalizálásával."

**Dia 38: LoRA: Low-Rank Adaptation (Alacsony Rangú Adaptáció)** ([source: 76])

* **Téma:** A LoRA alapötlete.
* **Tudnivalók:** Probléma: Minden egyes downstream feladathoz külön Δθ paraméterváltozást kell tárolni, ami |Δθ| = |θ₀| méretű ([source: 77]). Ez óriási modelleknél (pl. GPT-3 175B) rendkívül költséges tárolás és telepítés szempontjából ([source: 77]). **Kulcsötlet:** A feladatspecifikus paraméter növekményt (Δθ) kódoljuk egy sokkal kisebb méretű paraméterhalmazzal (Θ), ahol |Θ| << |θ₀| ([source: 77]). A cél Δθ megtalálása helyett Θ optimalizálása lesz ([source: 78]).
* **Megértendő:** Ahelyett, hogy a teljes, nagy méretű változást (Δθ) tárolnánk minden feladathoz, a LoRA megtanul egy kis méretű "receptet" (Θ), ami alapján legenerálható a szükséges nagy méretű változás (Δθ).
* **Elmondandó:** "Itt jön a probléma: ha minden új feladathoz (összegzés, fordítás, kérdés-válasz stb.) egy teljes, 175 milliárd paraméteres változást (Δθ) kellene tárolnunk, az kezelhetetlen lenne. A LoRA zseniális ötlete az, hogy feltételezi, ez a hatalmas Δθ változás valójában leírható ('kódolható') egy sokkal-sokkal kisebb paraméterkészlettel, amit Θ-val jelölünk. Tehát ahelyett, hogy a nagy Δθ-t keresnénk, a kis Θ-t optimalizáljuk."

**Dia 39: Alacsony Rangú Paraméterezett Frissítési Mátrixok** ([source: 79])

* **Téma:** A LoRA matematikai megvalósítása.
* **Tudnivalók:** Megfigyelés: A súlymátrixok frissítései (ΔW) az adaptáció során gyakran "alacsony belső rangúak" (low intrinsic rank) ([source: 79]). Legyen W₀ egy előtanított súlymátrix (d x k méretű) ([source: 79]). A frissítését (ΔW) egy alacsony rangú felbontással korlátozzuk: W₀ + ΔW = W₀ + BA, ahol B egy d x r mátrix, A egy r x k mátrix, és a rang r << min(d, k) ([source: 79], [source: 80]). Csak A és B tartalmaz tanítható paramétereket ([source: 80]).
* **Megértendő:** Egy nagy mátrix (ΔW) helyett két kicsi mátrixot (B és A) tanítunk meg, amelyek szorzata közelíti a nagy mátrixot. A tanítandó paraméterek száma drasztikusan csökken (d*k helyett d*r + r*k).
* **Elmondandó:** "Hogyan kódolja a LoRA a nagy változást (ΔW) kis paraméterekkel (Θ)? Úgy, hogy kihasználja azt a megfigyelést, hogy ezek a ΔW frissítési mátrixok gyakran 'alacsony rangúak', ami matematikailag azt jelenti, hogy előállíthatók két sokkal 'vékonyabb' mátrix szorzataként. Tehát ahelyett, hogy a teljes d x k méretű ΔW mátrixot tanítanánk, csak egy d x r méretű B és egy r x k méretű A mátrixot tanítunk, ahol 'r' (a rang) egy kicsi szám (pl. 8, 16, 32). A tényleges frissítés pedig e két kis mátrix szorzata: ΔW = BA. Csak A-t és B-t kell tanítani és tárolni!"

**Dia 40: LoRA Tulajdonságok** ([source: 81])

* **Téma:** A LoRA gyakorlati előnyei és jellemzői.
* **Tudnivalók:**
    * Ahogy növeljük a tanítható paraméterek számát (azaz a rangot, r), a LoRA konvergál a teljes modell tanításához ([source: 81]).
    * **Nincs extra következtetési késleltetés:** Használatkor a megtanult BA szorzatot egyszerűen hozzá lehet adni az eredeti W₀ súlymátrixhoz (W = W₀ + BA). Egy másik feladatra váltáskor csak ki kell vonni az egyik BA-t és hozzáadni a másikat ([source: 81]).
    * Gyakran csak a self-attention modul súlymátrixaira alkalmazzák ([source: 81]).
* **Megértendő:** A LoRA rugalmas (a rang állítható), és ami nagyon fontos, a tanítás után nem lassítja a modell működését, mert a kis mátrixok hatása "beépíthető" az eredeti súlyokba.
* **Elmondandó:** "A LoRA rangja (r) egy hiperparaméter, amit hangolhatunk. Minél nagyobb r-t választunk, annál több paramétert tanítunk, és annál közelebb kerülünk a teljes finomhangoláshoz. Egy óriási előnye, hogy a használat (következtetés) során nincs extra számítási költsége! Mivel a B és A mátrixok fixek a tanítás után, a szorzatukat (BA) egyszer kiszámolhatjuk és hozzáadhatjuk az eredeti W₀ súlyokhoz. Így a modell ugyanolyan gyors marad, mint az eredeti. Ha feladatot váltunk, csak egy másik BA mátrixot kell hozzáadni. Gyakran elegendő csak a Transformer figyelmi mechanizmusának súlyaira alkalmazni."

**Dia 41: LoRA Teljesítmény (GPT-2)** ([source: 82])

* **Téma:** LoRA kísérleti eredményei GPT-2 modellen.
* **Tudnivalók:** Az ábra a GPT-2 közepes (M) és nagy (L) változatain mutatja a LoRA teljesítményét az E2E NLG (szöveggenerálási) kihíváson, összehasonlítva más adaptációs módszerekkel. A LoRA felülmúlja a baseline-okat kevesebb vagy hasonló számú tanítható paraméterrel ([source: 82], [source: 83]). (Magasabb metrika érték a jobb).
* **Megértendő:** A LoRA a gyakorlatban is jól működik, kevesebb paraméterrel hozza vagy felülmúlja a drágább módszerek teljesítményét.
* **Elmondandó:** "Nézzünk konkrét eredményeket. Ez az ábra a GPT-2 modellen mutatja a LoRA teljesítményét egy szöveggenerálási feladaton. Látható, hogy a LoRA (piros) jobb eredményeket ér el, mint több más, hasonlóan kevés paramétert használó módszer (pl. Adapterek - zöld), és néha még a teljes finomhangolást is megközelíti vagy meghaladja, miközben drasztikusan kevesebb paramétert tanít."

**Dia 42: LoRA Skálázhatóság (GPT-3)** ([source: 85])

* **Téma:** LoRA teljesítménye a sokkal nagyobb GPT-3 modellen.
* **Tudnivalók:** Az ábra mutatja, hogy a LoRA a 175 milliárd paraméteres GPT-3 modellen is eléri vagy meghaladja a teljes finomhangolás (zöld vonal) teljesítményét különböző feladatokon (WebNLG, MultiNLI, SAMSum) ([source: 85]). Ez mutatja a LoRA jó skálázhatóságát és feladat-teljesítményét ([source: 85]).
* **Megértendő:** A LoRA nemcsak kisebb modelleken működik, hanem a legnagyobb nyelvi modellek esetében is hatékony és eredményes adaptációs technika.
* **Elmondandó:** "És ami még fontosabb: a LoRA nemcsak a 'kisebb' GPT-2-n működik, hanem a gigantikus, 175 milliárd paraméteres GPT-3-on is! Ezek az eredmények azt mutatják, hogy a LoRA képes elérni vagy akár meg is haladni a teljes finomhangolás pontosságát, miközben a tanított paraméterek számának csak a töredékét igényli. Ez óriási előny ilyen hatalmas modelleknél."

**Dia 43: Az alacsony rangú adaptáció megértése** ([source: 86])

* **Téma:** Valószínűleg egy vizuális magyarázat vagy mélyebb betekintés a LoRA működésébe.
* **Tudnivalók:** A dia tartalma nem látható teljesen, de valószínűleg ábrákkal vagy további matematikai részletekkel magyarázza az alacsony rangú közelítés lényegét.
* **Megértendő:** Az alacsony rangú felbontás mögötti intuíció vagy matematikai háttér.
* **Elmondandó:** (Az aktuális dia tartalmától függően) "Ez az ábra/részlet segít jobban megérteni, miért is működik ez az alacsony rangú közelítés..."

**Dia 44: LoRA-tól a QLoRA-ig** ([source: 87])

* **Téma:** A QLoRA mint a LoRA továbbfejlesztése.
* **Tudnivalók:** A QLoRA (Quantized LoRA) továbbfejleszti a LoRA-t azáltal, hogy:
    1.  A fő Transformer modellt **kvantálja** 4 bites pontosságra (jelentős memóriacsökkentés).
    2.  Egy új, információelméletileg optimális 4 bites adattípust használ (NF4 - NormalFloat4) a normális eloszlású súlyokhoz ([source: 87]).
    3.  "Oldalazott optimalizálót" (paged optimizer) használ a memória-csúcsok kezelésére a tanítás során ([source: 87]).
* **Megértendő:** A QLoRA még tovább csökkenti a LoRA-alapú finomhangolás memóriaigényét azáltal, hogy az eredeti modell súlyait alacsonyabb pontosságon tárolja, miközben a LoRA mátrixokat továbbra is nagyobb pontossággal tanítja.
* **Elmondandó:** "A LoRA már önmagában is nagyon hatékony, de lehet még tovább fokozni. A QLoRA ötlete az, hogy az eredeti, hatalmas modell (pl. GPT-3) súlyait ne a szokásos 16 vagy 32 bites pontossággal tároljuk a memóriában, hanem csak 4 biten! Ez drasztikusan csökkenti a memóriaigényt. Erre egy speciális, normális eloszlású súlyokra optimalizált 4 bites formátumot (NF4) használnak. Eközben a kis LoRA mátrixokat (A és B) továbbra is nagyobb pontossággal tanítják. A QLoRA lehetővé teszi, hogy akár egyetlen fogyasztói GPU-n is finomhangoljunk óriási modelleket."

**Dia 45: Bemeneti Perspektíva: Prefix-Tuning** ([source: 89])

* **Téma:** Az adaptáció másik nézőpontja: a bemenet módosítása.
* **Tudnivalók:** A **Prefix-Tuning** során nem a modell belső súlyait módosítjuk, hanem a bemeneti szekvencia elé illesztünk egy sor tanítható, folytonos vektort (prefix paramétereket) ([source: 89], [source: 90]). Az eredeti modell (Transformer, LSTM stb.) paraméterei teljesen "befagyasztva" maradnak ([source: 90]).
* **Megértendő:** Itt a feladatspecifikus tudást nem a modell súlyainak módosításával, hanem egy tanítható "előtag" (prefix) formájában adjuk a modellnek a bemeneten.
* **Elmondandó:** "Most váltsunk nézőpontot! A paraméter-hatékony módszerek mellett léteznek olyanok is, amik a modell *bemenetét* manipulálják. Ilyen a Prefix-Tuning. Itt az eredeti modellhez egyáltalán nem nyúlunk hozzá, minden paramétere fix marad. Ehelyett minden bemeneti példa elé odateszünk néhány 'virtuális tokent', vagyis tanítható vektort – ez a 'prefix'. A modell ezeket a vektorokat ugyanúgy dolgozza fel, mint a valódi szavakat, és ezek a tanult prefixek irányítják a modell viselkedését a specifikus feladatra."

**Dia 46: Prefix-Tuning / Prompt Tuning Részletek** ([source: 91])

* **Téma:** A Prefix-Tuning és a Prompt Tuning működésének pontosítása.
* **Tudnivalók:** A Prefix-Tuning tanítható paramétereket (prefix) ad hozzá, az előtanított paraméterek befagyasztva maradnak ([source: 91]). A prefixet a modell ugyanúgy dolgozza fel, mint a valódi szavakat ([source: 92]). Előny: következtetéskor egy batch-en belül minden elemhez tartozhat más-más tanult prefix (tehát más "finomhangolt" modell) ([source: 93]). (Megjegyzés: A Prompt Tuning [source: 98] nagyon hasonló, de általában csak a bemeneti réteghez ad tanítható vektorokat, míg a Prefix-Tuning [source: 94] a Transformer minden rétegének aktivációit befolyásolhatja a prefixszel.)
* **Megértendő:** A tanult prefix/prompt vektorok a modell rejtett állapotait módosítják, így irányítva a kimenetet a kívánt feladatra. Rugalmas, mert egy modellen belül több feladat prefixét is lehet kezelni egyszerre.
* **Elmondandó:** "Tehát a Prefix-Tuning (és a hozzá nagyon hasonló Prompt Tuning) lényege, hogy tanítható vektorokat adunk a bemenethez. Ezek a vektorok befolyásolják a modell belső működését anélkül, hogy az eredeti súlyokat megváltoztatnánk. Nagy előnye, hogy mivel csak a bemenet változik, egyetlen betöltött nagy modell képes lehet egyszerre több különböző feladatot is ellátni, csak a megfelelő prefixet/promptot kell elé tenni."

**Dia 47: Többrétegű Prompt Tuning Optimalizálása (P-Tuning v2)** ([source: 95])

* **Téma:** A prompt tuning továbbfejlesztése: tanítható paraméterek több rétegben.
* **Tudnivalók:** Ahelyett, hogy csak a bemeneti rétegben lennének tanítható paraméterek (mint az eredeti Prompt Tuningnál), a P-Tuning v2 (és hasonló módszerek) a modell *minden egyes rétegében* elhelyez tanítható prompt vektorokat ([source: 95], [source: 96]).
* **Megértendő:** Ha a tanítható "irányító" vektorokat nemcsak a legelejére, hanem a modell mélyebb rétegeibe is beillesztjük, az nagyobb kapacitást ad a modellnek az adaptációra.
* **Elmondandó:** "Az eredeti Prompt Tuning, ami csak a bemeneti réteghez adott tanítható vektorokat, néha nem elég erős komplexebb feladatokhoz. Ezért jöttek létre olyan továbbfejlesztett változatok, mint a P-Tuning v2, ahol nemcsak az elejére, hanem a Transformer modell minden egyes rétegébe beillesztenek néhány tanítható vektort. Ez sokkal több 'belenyúlási' lehetőséget ad a modell működésébe, így hatékonyabb adaptációt tesz lehetővé."

**Dia 48: A (Bemeneti) Prompt Tuning Skálázódási Problémái** ([source: 97])

* **Téma:** Miért nem mindig elég hatékony a csak bemeneti rétegre ható prompt tuning?
* **Tudnivalók:** Azok a módszerek, amelyek csak a bemeneti rétegben adnak hozzá tanítható paramétereket (mint a standard Prompt Tuning), korlátozott kapacitással rendelkeznek az adaptációhoz ([source: 97]). Ezért gyengébben teljesítenek kisebb modellméreteknél és nehezebb feladatokon ([source: 97], [source: 98]), összehasonlítva például a LoRA-val vagy az Adapterekkel, amik több paramétert módosítanak.
* **Megértendő:** A modell adaptálásához szükséges kapacitás (tanítható paraméterek száma és helye) fontos. A túl kevés tanítható paraméter (mint a sima prompt tuningnál) korlátozhatja a teljesítményt.
* **Elmondandó:** "Egy fontos tanulság, hogy a legegyszerűbb Prompt Tuning (ami csak a bemenethez ad tanítható vektorokat) teljesítménye erősen függ a modell méretétől. Kisebb modelleknél vagy nehezebb feladatoknál gyakran alulteljesít a többi PEFT módszerhez (pl. LoRA, Adapterek) képest. Ennek oka valószínűleg az, hogy túl kevés tanítható paramétert biztosít a komplexebb adaptációhoz."

**Dia 49: Funkcionális Perspektíva: Függvénykompozíció** ([source: 99])

* **Téma:** Az adaptáció harmadik nézőpontja: a modell funkcióinak módosítása.
* **Tudnivalók:** Ez a megközelítés a modell meglévő funkcióit egészíti ki új, feladatspecifikus funkciókkal ([source: 99]). Gyakran használják többcélú tanulásban (multi-task learning), ahol különböző feladatokhoz tartozó modulokat komponálnak össze ([source: 99], [source: 100]).
* **Megértendő:** Ahelyett, hogy a meglévő paramétereket vagy a bemenetet módosítanánk, új funkcionális blokkokat (modulokat) adunk a modellhez.
* **Elmondandó:** "Végül nézzük meg a harmadik nézőpontot, a funkcionális perspektívát. Itt az alapötlet az, hogy nem a meglévő részeket piszkáljuk, hanem teljesen új 'funkcionális egységeket' vagy modulokat adunk a modellhez, amelyek a specifikus feladatot végzik el. Ez hasonlít a többcélú tanuláshoz, ahol egy alapmodellre építenek rá feladatspecifikus 'fejeket' vagy rétegeket."

**Dia 50: Adapter (Houlsby et al. 2019)** ([source: 101])

* **Téma:** Az Adapter modulok bemutatása.
* **Tudnivalók:** Az Adapterek kis neurális hálózat modulok (f_θ), amelyeket az előtanított modell rétegei *közé* illesztenek be, hogy adaptálják a modellt egy downstream feladatra ([source: 101]). Egy tipikus Adapter egy Transformer rétegben:
    1.  Egy lefelé vetítő feed-forward réteg (W_down, szűkítés) ([source: 101]).
    2.  Egy nemlinearitás (pl. ReLU, GeLU) ([source: 102]).
    3.  Egy felfelé vetítő feed-forward réteg (W_up, bővítés az eredeti dimenzióra) ([source: 101]).
    4.  Egy reziduális kapcsolat (az eredeti aktiváció hozzáadása) ([source: 102]).
    A finomhangolás során csak az Adapterek paraméterei (W_down, W_up) frissülnek, az eredeti modell súlyai befagyasztva maradnak.
* **Megértendő:** Az Adapterek kis "betétek" a nagy modell rétegei között, amik megtanulják a feladatspecifikus transzformációkat anélkül, hogy az eredeti modellhez hozzá kellene nyúlni. A szűkítés-bővítés (bottleneck) struktúra biztosítja, hogy kevés új paraméter legyen.
* **Elmondandó:** "Ennek a funkcionális megközelítésnek az egyik legnépszerűbb példája az 'Adapter' modul. Ezek apró, jellemzően két lineáris rétegből és egy nemlinearitásból álló kis hálózatok, amiket 'beszúrunk' az eredeti nagy modell (pl. Transformer) rétegei közé. A trükk az, hogy az első réteg lecsökkenti a dimenziót (szűkít), a második pedig visszaállítja (bővít). Csak ezeknek a kis adapter moduloknak a súlyait tanítjuk, az eredeti modell súlyai változatlanok maradnak. A végén az adapter kimenetét hozzáadjuk az eredeti réteg kimenetéhez (reziduális kapcsolat)."

**Dia 51: Adapter Elhelyezése** ([source: 103])

* **Téma:** Hol helyezkednek el az Adapterek egy Transformer blokkban?
* **Tudnivalók:** Az Adaptereket általában a Transformer blokkon belül a multi-head attention réteg *után* és/vagy a feed-forward réteg *után* szokták elhelyezni ([source: 103]). A legtöbb megközelítés a szűkített (bottleneck) dizájnt használja lineáris rétegekkel ([source: 103]).
* **Megértendő:** Az Adapterek stratégiai pontokon illeszkednek a modellbe, hogy hatékonyan tudják módosítani az információáramlást.
* **Elmondandó:** "Hol helyezkednek el ezek az adapterek? Egy tipikus Transformer blokkban két fő komponens van: a figyelmi mechanizmus és a feed-forward hálózat. Az adaptereket általában ezek *után* szokták beilleszteni, ahogy az ábrán is látszik. Így mindkét fő komponens kimenetét képesek finomítani a feladatnak megfelelően."

**Dia 52: Adapterek: Pontosság vs. Paraméterszám** ([source: 104])

* **Téma:** Az Adapterek teljesítményének összehasonlítása a teljes finomhangolással.
* **Tudnivalók:** Az ábra a GLUE benchmark 9 feladatán mutatja a teljesítményt a tanított paraméterek számának függvényében ([source: 106]). Az Adapter alapú hangolás (Adapter Tuning) eléri a teljes finomhangoláshoz (Full Finetuning) hasonló teljesítményt, de nagyságrendileg (kb. 100-szor) kevesebb tanított paraméterrel ([source: 107]).
* **Megértendő:** Az Adapterek kiváló kompromisszumot kínálnak a pontosság és a paraméterhatékonyság között.
* **Elmondandó:** "És mennyire jók ezek az Adapterek? Ez a grafikon azt mutatja, hogy az Adapterekkel (piros görbe) majdnem ugyanolyan jó pontosságot lehet elérni, mint a teljes modell finomhangolásával (zöld sáv), de mindezt körülbelül századannyi tanítható paraméterrel! Ez óriási megtakarítást jelent mind a tanítási időben, mind a tárhelyigényben, ha sok különböző feladatra akarjuk adaptálni a modellt."

**Dia 53: Nyelvi Adapterek? Feladattudás vs. Nyelvi Tudás** ([source: 108])

* **Téma:** Az Adapterek használata nemcsak feladatokra, hanem nyelvekre/dialektusokra is.
* **Tudnivalók:** Az Adapterek olyan transzformációkat tanulnak meg, amelyek a mögöttes modellt alkalmasabbá teszik egy adott feladatra *vagy nyelvre* ([source: 108]). Példa: Maszkolt nyelvi modellezés (MLM) segítségével lehet nyelvspecifikus adaptereket tanítani (pl. angol, kecsua), amiket aztán egy általános modellel kombinálhatunk ([source: 109]).
* **Megértendő:** Az adapter koncepció általánosítható: nemcsak egy új *feladatot* tanulhat meg egy adapter, hanem egy új *nyelv* vagy *dialektus* sajátosságait is.
* **Elmondandó:** "Az Adapterek nemcsak új *feladatok* megtanulására jók, hanem akár új *nyelvek* vagy *dialektusok* adaptálására is! Képzeljük el, hogy van egy nagy, angolul előtanított modellünk. Taníthatunk külön adaptereket például spanyolra, németre, vagy akár egy ritkább nyelvre, mint a kecsua, úgy, hogy csak az adaptert tanítjuk az adott nyelvű szövegeken. Így az alapmodell általános tudását kombinálhatjuk a nyelvspecifikus adapterrel."

**Dia 54: Adapterek használata dialektus adaptációra** ([source: 110])

* **Téma:** Konkrét példa: LLM-ek adaptálása különböző angol dialektusokra.
* **Tudnivalók:** LLM-eket, amelyeket standard amerikai angolon tanítottak, lehet adaptálni más angol dialektusokra (pl. brit angol, indiai angol) dialektus-specifikus adapterek segítségével ([source: 110]). Ezek kombinálhatók a feladatspecifikus adapterekkel is ([source: 110]).
* **Megértendő:** Az adapterek modulárisak: egy alapmodellre rátehetünk egy nyelvi/dialektus adaptert és egy feladat adaptert is.
* **Elmondandó:** "Itt egy konkrét példa: van egy standard amerikai angolon tanított alapmodellünk. Külön taníthatunk 'dialektus adaptereket' például brit angolra, ausztrál angolra stb. Ha most egy specifikus feladatot akarunk megoldani (pl. kérdés-válasz) brit angolul, akkor az alapmodellre rátehetjük a brit angol adaptert ÉS a kérdés-válasz feladat adapterét is. Ez a modularitás az adapterek egyik nagy előnye."

**Dia 55: Átskálázás (Rescaling)** ([source: 111])

* **Téma:** Egy még egyszerűbb PEFT módszer: csak skálázási faktorok tanítása.
* **Tudnivalók:** Egy funkció megtanulása helyett néha elég csak annak *átskálázása* elemenkénti szorzással ([source: 111]). Ezt gyakran alkalmazzák normalizációs rétegek paramétereire (pl. Batch Normalization a CV-ben, Layer Normalization az NLP-ben) ([source: 111]). Lehetővé teszi, hogy a modell kiválassza, mely jellemzők fontosabbak vagy kevésbé fontosak egy adott feladathoz ([source: 111]). Kompatibilis más módszerekkel (pl. a LoRA is tartalmaz egy tanítható skalár paramétert) ([source: 111]).
* **Megértendő:** Néha nincs szükség bonyolult új funkciókra, elég csak a meglévő aktivációk vagy paraméterek fontosságát (skáláját) megtanulni a feladathoz. Ez egy rendkívül paraméter-hatékony módszer.
* **Elmondandó:** "Létezik egy még az Adaptereknél is egyszerűbb funkcionális megközelítés: az átskálázás. Itt nem tanítunk új rétegeket, csak néhány szorzótényezőt tanulunk meg, amikkel a modell belső aktivációit vagy normalizációs paramétereit módosítjuk. Ez olyan, mintha a modell megtanulná 'felhangosítani' vagy 'lehalkítani' a különböző belső jeleket az adott feladatnak megfelelően. Meglepően hatékony tud lenni, és nagyon kevés plusz paramétert igényel."

**Dia 56: Paraméter Generálás (HyperNetworks)** ([source: 112])

* **Téma:** Modul paramétereinek generálása egy másik hálózattal.
* **Tudnivalók:** Eddig a különböző feladatokhoz tartozó modulokat (pl. adaptereket) külön-külön optimalizáltuk ([source: 112]). De mi van, ha ezek a modulok megoszthatnának valamilyen mögöttes struktúrát (mint a multi-task learningben)? Használhatunk egy kis neurális hálózatot – egy **hypernetworköt** – arra, hogy *generálja* a modul (pl. adapter) paramétereit ([source: 112]). Ez különösen hatékony, ha a generálást releváns metaadatok (pl. feladat leírása, nyelv azonosítója) alapján végezzük ([source: 112]).
* **Megértendő:** Ahelyett, hogy minden feladathoz külön tárolnánk az adapter súlyait, tanítunk egy kis "generátor" hálózatot (hypernetwork), ami képes legenerálni a szükséges adapter súlyokat a feladat leírása alapján.
* **Elmondandó:** "Eddig úgy tanítottuk az adaptereket, hogy minden feladathoz külön-külön optimalizáltuk a saját kis súlyait. De mi lenne, ha ezeket a súlyokat nem direktben tanítanánk, hanem egy másik, kis neurális hálózattal – egy úgynevezett 'hypernetworkkel' – generáltatnánk le? Ez a hypernetwork kapna valamilyen információt a feladatról (pl. egy feladat-beágyazást vagy nyelvi kódot), és ennek alapján 'kiköpné' a megfelelő adapter paramétereket. Ez lehetővé teszi a tudásmegosztást a feladatok között, és még hatékonyabbá teheti a tárolást."

**Dia 57: HyperNetwork Alkalmazások** ([source: 113])

* **Téma:** Mire használtak már hypernetworköket PEFT kontextusban?
* **Tudnivalók:** Hypernetworköket használtak már különböző modulparaméterek generálására:
    * Osztályozó fejek (classifier heads) ([source: 113]).
    * Folytonos promptok (continuous prompts) ([source: 114]).
    * Adapter rétegek ([source: 114], [source: 115]).
    A generálást kondicionálhatják:
    * Feladat beágyazásokra (Task embeddings)
    * Nyelvi beágyazásokra (Language embeddings)
    * Réteg azonosítóra (Layer ID) (pl. Hyper-X [source: 115]).
* **Megértendő:** A hypernetwork egy rugalmas eszköz, amivel különböző típusú PEFT modulok paramétereit lehet generálni, figyelembe véve a feladat, nyelv vagy akár a modellbeli pozíció kontextusát.
* **Elmondandó:** "Ez a hypernetwork ötlet elég általános. Használták már osztályozók utolsó rétegének generálására, a Prefix-Tuningnál látott folytonos prompt vektorok generálására, és persze Adapter rétegek paramétereinek generálására is. A hypernetwork bemeneteként szolgálhat a feladat leírása, a nyelv azonosítója, vagy akár az is, hogy a modell hanyadik rétegébe szánjuk az adaptert, így még specifikusabb paramétereket tud generálni."

**Dia 58: Egységesítő Nézet** ([source: 116])

* **Téma:** A különböző PEFT módszerek közötti kapcsolatok.
* **Tudnivalók:** He et al. [2022] megmutatták, hogy a LoRA, a Prefix Tuning és az Adapterek hasonló funkcionális formával leírhatók ([source: 116]). Mindegyik módszer felfogható úgy, mint ami módosítja a modell rejtett reprezentációit (h) ([source: 116]). A ritkaság, struktúra, alacsony rangú közelítések, átskálázás és egyéb tulajdonságok kombinálhatók ([source: 116]).
* **Megértendő:** Bár a LoRA, Adapterek, Prefix Tuning látszólag különbözőek, egy mélyebb szinten mind a modell belső információfeldolgozását módosítják célzottan és hatékonyan. Ezek a technikák nem zárják ki egymást, kombinálhatók is.
* **Elmondandó:** "Érdekes módon, bár ezek a módszerek – LoRA, Prefix Tuning, Adapterek – elsőre különbözőnek tűnnek, kimutatták, hogy matematikailag visszavezethetők egy közös alapformára. Mindegyik valamilyen módon a modell belső rejtett állapotait (aktivációit) módosítja. Ez azt is jelenti, hogy ezek a technikák nem feltétlenül zárják ki egymást; elméletileg akár kombinálni is lehet őket, például egy LoRA-t adapterekkel."

**Dia 59: Teljesítmény Összehasonlítás** ([source: 117])

* **Téma:** Különböző PEFT módszerek (pl. Prompt Tuning, Adapter, LoRA) teljesítményének és paraméterszámának vizuális összehasonlítása.
* **Tudnivalók:** Az ábra általában azt mutatja, hogy a Prompt Tuning (a legegyszerűbb, bemeneti) alulteljesít a korlátozott kapacitása miatt ([source: 117]). Az Adapterek jó teljesítményt nyújtanak, de több paramétert adnak hozzá (ami növelheti a késleltetést, bár a tanításuk hatékony) ([source: 117]). A LoRA gyakran jó kompromisszumot kínál (jó teljesítmény, kevés paraméter, nincs inferencia késleltetés).
* **Megértendő:** Nincs egyetlen "legjobb" PEFT módszer minden helyzetre. A választás függ a feladattól, a rendelkezésre álló erőforrásoktól, a kívánt pontosságtól és a megengedhető inferencia-késleltetéstől.
* **Elmondandó:** "Ez a grafikon (vagy táblázat) egy tipikus összehasonlítást mutat a különböző PEFT módszerek között. Gyakran látható, hogy a legegyszerűbb Prompt Tuning elmarad a többitől. Az Adapterek nagyon jók lehetnek, de kicsit több paramétert adnak hozzá. A LoRA sokszor jó egyensúlyt képvisel a pontosság, a kevés paraméter és a gyors inferencia között. A választás mindig a konkrét igényektől függ."

**Dia 60: Modulok Közösségi Megosztása (AdapterHub)** ([source: 118])

* **Téma:** Platform adapter modulok megosztására és újrafelhasználására.
* **Tudnivalók:** Az AdapterHub.ml egy online platform, ahol kutatók és fejlesztők megoszthatnak és letölthetnek előtanított adapter modulokat különböző nyelvekre és feladatokra ([source: 118]).
* **Megértendő:** Léteznek közösségi erőfeszítések a PEFT modulok (különösen adapterek) megosztására, ami megkönnyíti azok újrafelhasználását és gyorsítja a fejlesztést.
* **Elmondandó:** "Ahogy az alapmodelleket (pl. BERT, GPT) megosztják, úgy logikus lenne megosztani a rájuk épülő PEFT modulokat is. Erre jött létre például az AdapterHub, egy online tárhely, ahonnan letölthetünk már kész, előtanított adaptereket különböző feladatokra és nyelvekre. Ez jelentősen meggyorsíthatja a munkát, hiszen nem kell mindent nulláról tanítani."

**Dia 61: A hatékony adaptáció egyéb változatai** ([source: 119])

* **Téma:** Más hatékonyságnövelő technikák említése (pl. Knowledge Distillation).
* **Tudnivalók:** A PEFT mellett más módszerek is léteznek a hatékonyság növelésére, például a **Tudásdesztilláció (Knowledge Distillation)**, ahol egy nagy, "tanár" modellt használnak egy kisebb, "diák" modell tanítására ([source: 119]). A cél itt egy eleve kisebb, hatékonyabb modell létrehozása.
* **Megértendő:** A PEFT a nagy modellek *adaptálásának* hatékonyságára fókuszál. A tudásdesztilláció inkább kisebb modellek *létrehozására* szolgál.
* **Elmondandó:** "Végül érdemes megemlíteni, hogy a PEFT mellett más utak is vannak a hatékonyság felé. Ilyen például a tudásdesztilláció, ahol egy nagy, okos 'tanár' modell tudását próbáljuk 'átdesztillálni' egy kisebb, gyorsabb 'diák' modellbe. Ez nem adaptáció, hanem egy új, kisebb modell létrehozása, de szintén a hatékonyságot célozza."

**Dia 62: Összefoglalás** ([source: 120])

* **Téma:** Az előadás fő pontjainak áttekintése.
* **Tudnivalók:** Ismétlés: Prompting, Bevezetés a PEFT-be, Pruning/alhálózatok, LoRA, Adapterek.
* **Megértendő:** Az előadás bemutatta a nagy modellek adaptálásának kihívásait és a legfontosabb paraméter-hatékony megoldásokat.
* **Elmondandó:** "Összefoglalva, a mai előadáson áttekintettük, hogyan fejlődtek a nagy nyelvi modellek a GPT-től a GPT-3-ig, és hogyan jelentek meg az emergent képességek, mint a zero-shot és few-shot tanulás prompting segítségével. Láttuk a prompting korlátait és a teljes finomhangolás költségeit, ami elvezetett minket a Paraméter-Hatékony Finomhangolás (PEFT) fontosságához. Megvizsgáltuk a PEFT három fő irányzatát: a ritkítást (Pruning), az alacsony rangú adaptációt (LoRA és QLoRA), valamint a funkcionális megközelítéseket, mint a Prefix/Prompt Tuning és az Adapterek. Remélem, átfogó képet kaptak erről a gyorsan fejlődő területről."