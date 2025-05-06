**1. Dia: Címlap** [cite: 1]

* **Tartalom:** Ez a dia bemutatja az előadás témáját: "Természetes Nyelvfeldolgozás Mély Tanulással" (Natural Language Processing with Deep Learning), a kurzus kódját (CS224N/Ling284), az előadót (Tatsunori Hashimoto), és a konkrét fókuszt: "Nyitott problémák és diszkusszió".
* **Magyarázat diákoknak:** Ez az első dia, ami megadja az óra keretét. Arról lesz szó, hogy a számítógépek hogyan értik meg és dolgozzák fel az emberi nyelvet (ez a természetes nyelvfeldolgozás, NLP) modern, mély tanulásnak nevezett módszerekkel. Különösen azokra a kérdésekre fogunk koncentrálni, amelyekre még nincs tökéletes válasz a területen – ezek a nyitott problémák.

**2. Dia: Előadás terve + Logisztika** [cite: 2]

* **Tartalom:** Itt a kurzussal kapcsolatos gyakorlati információk (határidők, poszter szekció) és az előadás menete található[cite: 2]. A terv: 1) A kurzus legfontosabb gondolatainak átismétlése. 2) A nyitott problémák rövid, de széleskörű (bár nem teljes) áttekintése. 3) Kérdések és válaszok az előadás után[cite: 3].
* **Magyarázat diákoknak:** Itt láthatjuk, miről fog szólni pontosan ez az óra. Először felidézzük a legfontosabb alapokat, amiket eddig tanultunk a gépi nyelvfeldolgozásról. Utána belevágunk a közepébe: megnézzük, milyen nagy kérdések foglalkoztatják most a kutatókat ezen a területen. Végül lesz lehetőség kérdezni.

**3. Dia: Főbb ötletek áttekintése** [cite: 4, 5]

* **Tartalom:** Ez a dia vizuálisan összefoglalja a kurzus során érintett kulcsfontosságú technológiákat és ötleteket:
    * **Szóvektorok (Word Vectors / Word2Vec):** Szavak jelentésének numerikus reprezentációja[cite: 4].
    * **Neurális NLP:** Egyszerű neurális hálózatok használata NLP feladatokra (pl. osztályozás)[cite: 4].
    * **RNN-ek/LSTM-ek:** Visszacsatolt neurális hálózatok szekvenciális adatok (mint a szöveg) feldolgozására[cite: 5].
    * **Szekvencia-szekvencia modellek figyelemmel (Sequence-to-sequence with attention):** Modellek, amelyek egyik szekvenciából (pl. mondat egyik nyelven) egy másikat generálnak (pl. mondat másik nyelven), figyelem mechanizmussal javítva[cite: 5].
    * **Transzformerek (Transformers):** Modern, hatékony architektúra, ami sok mai NLP modell alapja[cite: 5].
    * **Előtanítás (Pretraining):** Nagy mennyiségű szövegen tanított modellek, amelyek általános nyelvi tudást szereznek[cite: 6]. A példák (trivia, szintaxis, koreferencia, szemantika, hangulat, következtetés) azt mutatják, milyen sokféle nyelvi jelenséget tanulnak meg ezek a modellek[cite: 7, 8, 9, 10]. Fontos megjegyzés, hogy a modellek a szöveggel együtt a benne rejlő káros előítéleteket (rasszizmus, szexizmus) is megtanulhatják[cite: 10].
* **Magyarázat diákoknak (Fontos fogalmak):**
    * **Szóvektorok (Word Vectors):** Képzeljük el, hogy minden szónak van egy koordinátája egy térben. A hasonló jelentésű szavak közel vannak egymáshoz. A Word2Vec egy módszer ezeknek a koordinátáknak (vektoroknak) a megtanulására a szavak szövegbeli környezete alapján.
    * **Neurális Hálózat (Neural Network):** Az emberi agy idegsejtjei által inspirált matematikai modell. Rétegekből áll, és adatokból képes mintázatokat tanulni. A "feed-forward" azt jelenti, hogy az információ egy irányba áramlik a hálózaton.
    * **Softmax:** Egy függvény, amit gyakran használnak osztályozási feladatoknál a neurális hálózatok kimeneti rétegében, hogy a kimeneteket valószínűségekké alakítsák (összegük 1).
    * **Visszaterjesztés (Backpropagation):** Az algoritmus, amivel a neurális hálózatok "tanulnak". Kiszámolja, hogyan kell módosítani a hálózat belső paramétereit (súlyait), hogy a hibája csökkenjen.
    * **RNN (Recurrent Neural Network):** Olyan neurális hálózat, amelynek van "memóriája", képes figyelembe venni a korábbi információkat a szekvenciában. Jól használható szövegeknél, ahol a szavak sorrendje számít. Az **LSTM (Long Short-Term Memory)** az RNN egy fejlettebb változata, ami jobban kezeli a hosszú távú függőségeket a szövegben.
    * **Szekvencia-szekvencia (Seq2Seq) modellek:** Egyik szekvenciát (pl. angol mondat) alakítanak át egy másik szekvenciává (pl. magyar mondat). Ilyeneket használnak gépi fordításra vagy szövegösszefoglalásra.
    * **Figyelem Mechanizmus (Attention):** Lehetővé teszi a Seq2Seq modellek számára, hogy a bemeneti szekvencia releváns részeire "fókuszáljanak", amikor a kimeneti szekvencia egy adott részét generálják. Nagyon fontos újítás volt.
    * **Transzformerek (Transformers):** Egy modern neurális hálózati architektúra, ami nagyrészt a figyelem mechanizmusra épül. Rendkívül sikeres lett, mert hatékonyan tudja párhuzamosan feldolgozni a szavakat és jól kezeli a hosszú távú függőségeket. Sok mai nagy nyelvi modell (pl. GPT) erre épül.
    * **Előtanítás (Pretraining) és Finomhangolás (Fine-tuning):** Az előtanítás során egy modellt hatalmas mennyiségű általános szövegen tanítanak (pl. az internet szövegein), hogy általános nyelvi megértést szerezzen. Utána ezt az előtanított modellt egy specifikus feladatra (pl. hangulatelemzés) kisebb, célzott adathalmazon tovább tanítják – ez a finomhangolás.
    * **Koreferencia (Coreference):** Annak meghatározása, hogy a szövegben mely névmások vagy kifejezések ugyanarra a dologra vagy személyre utalnak (pl. "Anna elment a boltba. *Ő* vett tejet." - *Ő* Annára utal).
    * **Lexikális Szemantika (Lexical Semantics):** A szavak jelentésével foglalkozó terület.
    * **Hangulatelemzés (Sentiment Analysis):** Szövegek érzelmi töltetének (pozitív, negatív, semleges) meghatározása.
    * **Torzítás/Előítélet (Bias):** A modellek a tanítóadatokból nemcsak hasznos tudást, hanem a bennük rejlő társadalmi előítéleteket is megtanulhatják, ami méltánytalan vagy káros kimenetekhez vezethet.

**4. Dia: 1. Ötlet: Sűrű reprezentációk és disztribucionális szemantika** [cite: 11, 12]

* **Tartalom:** Ez a dia az első kulcsötletet részletezi: a **disztribucionális szemantikát**. Az alapelve: egy szó jelentését a környezetében gyakran előforduló szavak határozzák meg ("Egy szót a társaságáról ismerszik meg" - J. R. Firth)[cite: 11]. A Word2Vec ennek egy megvalósítása, ahol a szóvektorokat úgy tanuljuk meg, hogy megjósoljuk a környező szavakat[cite: 12].
* **Magyarázat diákoknak:** Az egyik legfontosabb ötlet a modern NLP-ben, hogy a szavak jelentését nem szótári definíciókkal, hanem a használatukkal ragadjuk meg. Ha két szó gyakran jelenik meg hasonló szavak társaságában (pl. "király" és "királynő" gyakran fordul elő az "uralkodik", "trón", "palota" szavak mellett), akkor a jelentésük is hasonló. A **sűrű reprezentációk** (dense representations) vagy **szóvektorok** ezt matematikailag valósítják meg: minden szóhoz egy számsorozat (vektor) tartozik, és a hasonló jelentésű szavak vektorai közel vannak egymáshoz a "jelentéstérben". A Word2Vec egy konkrét módszer ezeknek a vektoroknak a kiszámítására.

**5. Dia: 2. Ötlet: Mélység és neurális hálózatok** [cite: 13, 14, 17]

* **Tartalom:** A második nagy ötlet a **mély neurális hálózatok** használata. A dia kiemeli, hogy a nagyon mély (sok rétegű) hálózatok tanítása kihívást jelentett[cite: 13, 15]. Bemutatja a **maradék kapcsolatokat (residual connections)** mint egy trükköt, ami segít a tanításban[cite: 13]. Ahelyett, hogy a réteg kimenete $Layer(X^{(i-1)})$ lenne, a kimenet $X^{(i-1)} + Layer(X^{(i-1)})$ lesz[cite: 14]. Ez megkönnyíti a **gradiens áramlását** (a tanító jel visszaáramlását) és hajlamossá teszi a modellt az **identitás függvény** (azaz a bemenet változatlanul hagyása) megtanulására, ami segít a mélyebb hálózatoknál[cite: 17]. A veszteségi tájkép (loss landscape) vizualizációja mutatja, hogy a maradék kapcsolatokkal simább a tájkép, könnyebb jó megoldást találni[cite: 17].
* **Magyarázat diákoknak:** Minél "mélyebb" egy neurális hálózat (minél több rétege van), annál összetettebb mintázatokat képes megtanulni. Régebben azonban nagyon nehéz volt ezeket a mély hálózatokat hatékonyan tanítani, mert a tanító jel "elveszett" a sok rétegen keresztül visszafelé haladva. A **maradék kapcsolatok (residual connections)** egy okos trükk: minden rétegnek csak a *változást* kell megtanulnia az előző réteghez képest, ahelyett, hogy a teljes új reprezentációt kellene előállítania. Ez olyan, mintha "átugrási" lehetőséget adnánk az információnak a rétegek között, ami stabilabbá és könnyebbé teszi a tanítást. A **veszteségi tájkép** egy vizualizációja annak, hogy mennyire "jó" a modell különböző beállításokkal – a simább tájkép azt jelenti, hogy könnyebb megtalálni a legjobb beállítást.

**6. Dia: 3. Ötlet: Szekvencia modellek és számítási hatékonyság** [cite: 18]

* **Tartalom:** A harmadik ötlet a **szekvencia modellekkel** és a hatékonysággal foglalkozik. Bemutatja az RNN-eknél fellépő **eltűnő gradiensek (vanishing gradients)** problémáját: a távoli információkból származó tanító jel gyengül, így a modell nehezen tanulja meg a **hosszú távú függőségeket**[cite: 19, 20]. Ezzel szembeállítja a **Transzformereket**, amelyek jobban **párhuzamosíthatók** (gyorsabb a tanításuk) és hatékonyabban kezelik a függőségeket a szavak között, köszönhetően a figyelem mechanizmusnak[cite: 18, 21]. A dia a Transzformer dekóder egy blokkját is ábrázolja[cite: 21].
* **Magyarázat diákoknak:** Amikor szöveget dolgozunk fel, a szavak sorrendje és a közöttük lévő kapcsolatok (akár távoliak is) fontosak. Az RNN-ek (és LSTM-ek) jók voltak erre, de nehezen tanulták meg a nagyon távoli szavak közötti kapcsolatokat (pl. egy hosszú bekezdés elején és végén lévő mondatok kapcsolata) – ez az **eltűnő gradiensek** problémája[cite: 19]. A **Transzformerek** forradalmasították ezt. Másképp dolgozzák fel a szekvenciát, főleg a figyelem mechanizmusra támaszkodva, ami lehetővé teszi, hogy bármelyik szó közvetlenül "odafigyeljen" bármelyik másikra a mondatban. Emellett sokkal gyorsabban taníthatók, mert a számítások jobban **párhuzamosíthatók** (egyszerre végezhetők)[cite: 18].

**7. Dia: 4. Ötlet: Nyelvi modellezés és előtanítás** [cite: 22, 30]

* **Tartalom:** A negyedik kulcsgondolat a **nyelvi modellezés (language modeling)** mint "univerzális" **előtanítási** feladat[cite: 22]. A nyelvi modellezés célja a következő szó megjóslása egy adott szövegkörnyezetben. Ez a látszólag egyszerű feladat arra kényszeríti a modellt, hogy sokféle nyelvi tudást sajátítson el (ismét példák: trivia, szintaxis, koreferencia stb.). A dia bemutatja a **skálázási törvényeket (scaling laws)** is: nagyobb modellek és több számítási kapacitás (compute) általában jobb teljesítményhez (alacsonyabb veszteséghez) vezet[cite: 30].
* **Magyarázat diákoknak:** Hogyan lehet egy gépet megtanítani "általában" a nyelvre? Az egyik leghatékonyabb módszer a **nyelvi modellezés**: a gépnek hatalmas mennyiségű szöveget mutatunk, és a feladata az, hogy mindig jósolja meg a következő szót. Ahhoz, hogy ezt jól csinálja, meg kell tanulnia a nyelvtan szabályait, a szavak jelentését, a kontextust, sőt, egy bizonyos szintű "világtudást" is. Ez az **előtanítás**[cite: 22]. Az így kapott modellek utána már könnyebben finomhangolhatók konkrét feladatokra. A **skálázási törvények** azt mutatják, hogy minél nagyobb egy modell (több paramétere van) és minél több adatot és számítási kapacitást (pl. drága videokártyákon töltött időt) használunk a tanításra, annál jobban teljesít a modell[cite: 30]. De ez felveti a káros tartalmak és előítéletek megtanulásának problémáját is[cite: 30].

**8. Dia: Nyitott problémák - áttekintés** [cite: 31]

* **Tartalom:** Ez a dia elkezdi a nyitott problémák áttekintését. Hat fő területet sorol fel és illusztrál:
    * **Általánosítás (Generalization):** Mennyire működnek jól a modellek új, nem látott adatokon? (Példa: Adversarial QA - egy kis, irreleváns változtatás a bemeneten elrontja a választ)[cite: 32, 33].
    * **Analízis és megértés (Analysis and understanding):** Hogyan működnek a modellek belül? Mit tanulnak meg valójában? [cite: 31]
    * **Értékelés (Evaluations):** Hogyan mérjük a modellek teljesítményét megbízhatóan? (Példa: GLUE benchmark)[cite: 31].
    * **Területek + Modalitások (Domains + modalities):** Hogyan alkalmazhatók a modellek specifikus területeken (pl. orvostudomány [cite: 31]) vagy más típusú adatokkal (pl. képekkel)?
    * **Többnyelvűség (Multilingual):** Hogyan kezelik a modellek a különböző nyelveket? (Példa: felhasználók földrajzi eloszlása)[cite: 34].
    * **Méltányosság és társadalmi hatás (Fairness and social impact):** Milyen társadalmi következményei vannak a modelleknek, és hogyan tehetjük őket méltányosabbá? [cite: 34]
* **Magyarázat diákoknak:** Most rátérünk azokra a területekre, ahol még sok a kérdés és a tennivaló.
    * **Általánosítás:** Hiába tanul meg egy modell valamit a tanító adatokon, vajon új helyzetekben is helyt fog állni? A példa [cite: 32, 33] mutatja, hogy néha egy apró, ember számára jelentéktelen változtatás teljesen megzavarja a modellt. Ez azt jelzi, hogy nem biztos, hogy valódi megértés van mögötte.
    * **Megértés:** Ezek a modellek gyakran "fekete dobozként" működnek – nem látjuk pontosan, miért adnak egy adott választ[cite: 31]. Fontos lenne jobban megérteni a belső működésüket.
    * **Értékelés:** Hogyan mérjük, hogy egy modell tényleg "jó"-e? A jelenlegi tesztek (benchmarkok, mint a GLUE [cite: 31]) nem mindig tökéletesek.
    * **Új területek és adatok:** Hogyan használhatjuk ezeket a modelleket specifikus területeken, mint az orvostudomány [cite: 31] vagy a jog? És hogyan kombinálhatjuk a szöveget más adatokkal, például képekkel (multimodalitás)?
    * **Többnyelvűség:** A legtöbb modell angol nyelven a legjobb. Hogyan lehet elérni, hogy más nyelveken, különösen a kevés digitális adattal rendelkező (alacsony erőforrású) nyelveken is jól működjenek[cite: 34]?
    * **Méltányosság:** Hogyan biztosítsuk, hogy a modellek ne legyenek előítéletesek, ne terjesszenek sztereotípiákat, és ne érintsenek hátrányosan bizonyos csoportokat[cite: 34]?

**9. Dia: Megértik a modelljeink a feladatainkat?** [cite: 35, 38]

* **Tartalom:** Ez a dia tovább boncolgatja a megértés problémáját. Felteszi a kérdést, hogy a modellek valóban értik-e a feladatot, vagy csak **rövidítéseket (shortcuts)**, felszínes mintázatokat használnak[cite: 38]. Példák:
    * Az előző dián látott QA példa, ahol egy irreleváns mondat hozzáadása megváltoztatja a helyes választ, mert a modell valószínűleg csak az utolsó mondatra figyel[cite: 36, 37].
    * Egy **természetes nyelvi következtetés (NLI)** példa: a modellnek el kell döntenie, hogy egy "hipotézis" következik-e egy "premisszából". Itt a modell hibázik a **tagadás (negation)** miatt, pedig a premissza ("A gazdaság lehetne még jobb") és a hipotézis ("A gazdaság soha nem volt jobb") nyilvánvalóan ellentmondanak egymásnak[cite: 38].
* **Magyarázat diákoknak:** Képzeljük el, hogy egy diák csak a tankönyv utolsó mondatát olvassa el a vizsga előtt, és véletlenül helyesen válaszol pár kérdésre. Ettől még nem érti az anyagot. Hasonlóan, az NLP modellek is megtanulhatnak egyszerű trükköket ("rövidítéseket"), amikkel sokszor jó választ adnak, de ez nem jelent valódi megértést. Például, ha egy kérdésre válaszoló modell csak a kérdéshez legközelebb eső, hasonló szavakat tartalmazó mondatot nézi a szövegben, könnyen becsapható[cite: 36, 37]. A másik példa [cite: 38] a **természetes nyelvi következtetést (NLI)** mutatja be, ahol a gépnek logikai kapcsolatot kell felismernie mondatok között. Itt a modell láthatóan nem érti a tagadás jelentését.

**10. Dia: Mennyire általánosítanak a modellek? (Generalizáció)** [cite: 39]

* **Tartalom:** Tovább vizsgálja az általánosítás korlátait. Egy tanulmányra (Min, 2022) hivatkozva azt mutatja, hogy a modern nagy nyelvi modellek (LLM-ek) **kontextusban történő tanulása (In-Context Learning, ICL)** során szinte ugyanolyan jól teljesítenek akkor is, ha a példákban véletlenszerű címkéket kapnak, mint amikor helyes címkéket. Ez arra utal, hogy a modellek inkább a példák formai mintázatát (felszíni jeleket) használják ki, nem pedig a tartalmukból tanulnak a konkrét feladathoz[cite: 39]. A diagram az F1-pontszámot (egy osztályozási metrikát) mutatja különböző modelleknél (MetaICL, GPT-J, GPT-3) demonstráció nélkül, helyes címkés demonstrációval és véletlen címkés demonstrációval.
* **Magyarázat diákoknak:** A **kontextusban történő tanulás (ICL)** egy érdekes képessége a nagy nyelvi modelleknek: anélkül, hogy expliciten tanítanánk őket egy új feladatra, ha adunk nekik pár példát a feladatról a bemenetben (ezt hívják promptnak), képesek azt megoldani. Ez a dia viszont azt mutatja, hogy a modellek ezt talán nem is úgy csinálják, ahogy gondolnánk. Még akkor is javul a teljesítményük, ha a példákban a válaszok teljesen rosszak (véletlenszerűek)[cite: 39]. Ez arra utalhat, hogy a modell nem a példa logikáját érti meg, hanem csak felszínes mintázatokat követ (pl. milyen hosszú a válasz, milyen szavak vannak benne), és ezek a "jobb rövidítések" segítik a jobb teljesítményt[cite: 39]. Az **F1-pontszám** egy mérőszám arra, hogy mennyire pontos egy osztályozó modell.

**11. Dia: Hogyan lépjenek túl a modellek a tanító adaton? (Generalizáció)** [cite: 40]

* **Tartalom:** Felteszi a kérdést, hogyan érhetnénk el, hogy a modellek jobban, emberszerűbben általánosítsanak, akár kevés adatból is[cite: 40]. Hivatkozik a **SCAN adathalmazra**, ami a **szisztematikus általánosítást** teszteli (azaz, hogy a modell képes-e megtanult elemeket új, strukturált módon kombinálni)[cite: 41].
* **Magyarázat diákoknak:** Az emberek nagyon jól tudnak általánosítani kevés példából is. Ha megtanuljuk, mit jelent "ugrani", és látunk egy új tárgyat, valószínűleg tudjuk, mit jelent "átugrani" azt. A gépeknek ez nehezebb. A **szisztematikus általánosítás** azt a képességet jelenti, hogy a megtanult szabályokat vagy építőelemeket új, összetettebb helyzetekben is alkalmazni tudjuk. A **SCAN adathalmaz** [cite: 41] például olyan egyszerű parancsokból áll, mint "fuss", és arra teszteli a modellt, hogy képes-e megérteni az olyan kombinációkat, mint "fuss kétszer jobbra", még ha pontosan ezt a kombinációt nem is látta a tanítás során. A cél az, hogy a modellek jobban hasonlítsanak az emberi tanulásra (**kevés adatból való tanulás - few-shot learning**).

**12. Dia: Van több az IID hiba optimalizálásánál? (Generalizáció)** [cite: 42]

* **Tartalom:** Érdekes megfigyelést tesz: bár intuitívan mást gondolnánk, azok a modellek, amelyek átlagosan a legjobban teljesítenek a standard tesztadatokon (amik általában **IID**, azaz független és azonos eloszlásúak a tanító adatokkal), általában a **legrobusztusabbak** is (azaz jobban ellenállnak a kis zavaró tényezőknek vagy az eloszlásbeli eltéréseknek)[cite: 42].
* **Magyarázat diákoknak:** Az **IID (Independent and Identically Distributed)** feltételezés azt jelenti, hogy a tesztadatok ugyanolyan jellegűek és eloszlásúak, mint a tanító adatok. A legtöbb gépi tanulási modell ezt feltételezi. A **robusztusság** azt méri, hogy a modell mennyire működik jól akkor is, ha a bemeneti adatok kicsit mások, mint amiken tanult (pl. zajosabbak, vagy szokatlanabb stílusúak). Ez a dia azt mondja, hogy meglepő módon az a törekvés, hogy a modell minél jobb legyen a "szokásos" teszteken (IID hiba minimalizálása), úgy tűnik, együtt jár azzal is, hogy a modell ellenállóbb lesz a váratlan helyzetekkel szemben[cite: 42].

**13. Dia: Analízis és interpretáció** [cite: 43]

* **Tartalom:** Felteszi a kérdést, hogy miért működnek az NLP rendszerek, és hivatkozik egy XKCD képregényre, ami humorosan ábrázolja a gépi tanulási modellek "fekete doboz" jellegét és az **interpretálhatóság** nehézségeit[cite: 43].
* **Magyarázat diákoknak:** Miután létrehoztunk egy jól működő modellt, szeretnénk megérteni, *hogyan* és *miért* működik. Ez az **interpretálhatóság** vagy **magyarázhatóság (explainability)** területe. Miért hozta ezt a döntést? Milyen belső "gondolkodási" folyamat vezetett a válaszhoz? Ez nemcsak tudományos kíváncsiság, hanem a megbízhatóság és a hibakeresés miatt is fontos. Az XKCD képregény [cite: 43] arra utal, hogy gyakran csak egy nagy, bonyolult rendszert kapunk, aminek a belső működését nehéz kibogozni.

**14. Dia: Mi történik a neurális hálózatok belsejében? (Analízis)** [cite: 44, 45, 46]

* **Tartalom:** Kritizálja azt a gyakorlatot, hogy a modelleket csak egyetlen számmal (pl. pontossággal) jellemezzük[cite: 44]. Felteszi a kérdést: Mit tanulnak meg valójában? Miért sikeresek vagy miért hibáznak[cite: 45]? A modellt **fekete dobozként (black box)** ábrázolja[cite: 46].
* **Magyarázat diákoknak:** Gyakran egy modellt egyetlen számmal értékelünk, például "90%-os pontosság"[cite: 44]. De ez nem mond sokat arról, hogy a modell *mit tud* és *mit nem*. Lehet, hogy a maradék 10%-ban nagyon buta hibákat vét. Fontos lenne mélyebben megérteni, milyen tudást reprezentálnak ezek a **fekete doboz** modellek[cite: 46], miért működnek jól bizonyos esetekben, és miért vallanak kudarcot másokban[cite: 45].

**15. Dia: Régi eredmények interpretálható latens egységekről** [cite: 47, 48, 49]

* **Tartalom:** Bemutat egy korábbi kutatást (Karpathy et al., 2016)[cite: 47], amely azt találta, hogy egy karakter-szintű LSTM nyelvi modellben [cite: 48] egyes **latens egységek** (a rejtett rétegek neuronjai, vagy itt konkrétan az LSTM cellaállapotának dimenziói [cite: 48]) interpretálható funkciókat tanulnak meg (pl. idézőjelek közötti szöveg felismerése, sorhossz figyelése, zárójelek mélysége)[cite: 49].
* **Magyarázat diákoknak:** Bár a modellek gyakran fekete dobozok, néha találunk bennük olyan belső részeket (**latens egységeket**), amelyeknek úgy tűnik, van valami értelmes feladata. Ez a példa [cite: 47] egy olyan modellt mutat, ami karakterenként olvassa a szöveget. A kutatók azt találták, hogy a modell egyes belső "kapcsolói" (neuronjai) specializálódtak bizonyos dolgokra, például az egyik akkor "kapcsol be", ha idézőjelen belül van, egy másik pedig a sor végének közeledtét jelzi[cite: 49]. Ez reményt ad arra, hogy a modellek működése legalább részben megérthető.

**16. Dia: Építhetünk interpretálható, de jól teljesítő modelleket? (Analízis)** [cite: 50]

* **Tartalom:** Felteszi a kulcskérdést: Lehetséges-e olyan modelleket építeni, amelyek egyszerre nagyon jól teljesítenek a feladatukban, *és* könnyen érthető a működésük? Vagy ez a két cél ellentétes egymással[cite: 50]?
* **Magyarázat diákoknak:** Gyakran úgy tűnik, hogy minél bonyolultabb (és jobban teljesítő) egy modell, annál nehezebb megérteni. De vajon ez szükségszerű? Lehet-e olyan modelleket tervezni, amelyek ötvözik a jó teljesítményt az átláthatósággal[cite: 50]? Ez egy aktív kutatási terület.

**17. Dia: Építhetünk interpretálható, jól teljesítő modelleket?** [cite: 51]

* **Tartalom:** Megemlíti a **Backpack nyelvi modelleket** mint egy lehetséges irányt az interpretálhatóbb modellek felé[cite: 51].
* **Magyarázat diákoknak:** A **Backpack (hátizsák) nyelvi modellek** [cite: 51] egy kísérleti megközelítés. Az ötlet az, hogy a modell expliciten próbálja szétválasztani a nyelvtani (szintaktikai) és jelentésbeli (szemantikai) információkat külön "hátizsákokba", ami remélhetőleg könnyebben értelmezhetővé teszi a működését.

**18. Dia: Segíthet a megértés a következő transzformer megtalálásában? (Analízis)** [cite: 52, 53, 54]

* **Tartalom:** Összekapcsolja a jelenlegi modellek (mint a Transzformer [cite: 52]) megértését a jövőbeli fejlődéssel. Fontos kérdéseket vet fel[cite: 53, 54]:
    * Mit lehet és mit nem lehet megtanulni nyelvi modellezéssel történő előtanítással?
    * Mi fogja leváltani a Transzformert? Milyen lesz a következő generációs architektúra?
    * Mivel küzdenek a mély tanulási modellek? Mik a korlátaik?
    * Mit árulnak el a neurális modellek az emberi nyelvről?
    * Hogyan hatnak ezek a modellek az emberekre és a hatalmi viszonyokra?
* **Magyarázat diákoknak:** Ha jobban értjük, hogyan működnek a mai legjobb modellek (mint a Transzformer [cite: 52]), az segíthet abban, hogy még jobbakat fejlesszünk a jövőben. Ez a dia olyan alapvető kérdéseket tesz fel, amelyek a kutatás irányát szabják meg[cite: 53, 54]. Például: Milyen tudást szereznek meg a modellek a rengeteg szövegből, és mi az, amit nem? Vannak-e olyan feladatok, amikben a mai modellek alapvetően gyengék? Hogyan befolyásolják ezek a technológiák a társadalmat?

**19. Dia: Többnyelvűség** [cite: 55]

* **Tartalom:** Rámutat a jelentős teljesítménykülönbségekre a **magas erőforrású nyelvek** (mint az angol, ahol sok digitális adat van) és az **alacsony erőforrású nyelvek** (mint a telugu, ahol kevés adat van) között, még a legjobb modellek esetében is[cite: 55].
* **Magyarázat diákoknak:** A legtöbb NLP kutatás és fejlesztés angol nyelvre fókuszál, mert ehhez van a legtöbb könnyen elérhető adat (szöveg az internetről, könyvek stb.). Ezek a **magas erőforrású nyelvek**. Sok más nyelv (**alacsony erőforrású nyelvek**) esetében sokkal kevesebb ilyen adat áll rendelkezésre. Emiatt a modellek teljesítménye ezeken a nyelveken általában sokkal gyengébb[cite: 55]. Ez egy komoly méltányossági probléma is.

**20. Dia: Eltüntethetjük a nyelvi erőforrásbeli különbségeket? (Többnyelvűség)** [cite: 56, 57]

* **Tartalom:** Összekapcsolja a teljesítménybeli különbségeket az előtanításhoz rendelkezésre álló adatok mennyiségével, és felteszi a kérdést, hogyan lehetne ezt a szakadékot áthidalni[cite: 56, 57].
* **Magyarázat diákoknak:** Mivel a modellek az adatokból tanulnak, az adatok hiánya közvetlenül vezet a gyengébb teljesítményhez[cite: 56]. Hogyan tudnánk segíteni az alacsony erőforrású nyelveken? Hogyan szerezhetnénk vagy hozhatnánk létre több adatot számukra[cite: 57]?

**21. Dia: Munka extrém alacsony erőforrású nyelvekkel (Többnyelvűség)** [cite: 58]

* **Tartalom:** Kiemeli az **extrém alacsony erőforrású nyelvek** (sokszor csak beszélt, írásbeliség nélküli vagy kevés írott anyaggal rendelkező nyelvek) kihívásait: nincs géppel olvasható szöveg, sok ilyen nyelv veszélyeztetett (kihalhat), és kevés a piaci motiváció a támogatásukra, ami egy ördögi kört hoz létre[cite: 58]. Hivatkozik egy térképre (Adda et al 2016), ami a nyelvi sokféleséget/veszélyeztetettséget mutatja[cite: 58].
* **Magyarázat diákoknak:** A világ több ezer nyelvének nagy részéhez szinte semmilyen digitális adat nem létezik[cite: 58]. Sokukat a kihalás fenyegeti. Mivel nincs elég adat, nehéz NLP eszközöket fejleszteni hozzájuk, és mivel nincsenek ilyen eszközök, még nehezebb adatokat gyűjteni vagy a nyelvet életben tartani. Ez egy komoly kulturális és tudományos kihívás[cite: 58].

**22. Dia: Adatminőség változékonysága többnyelvű korpuszokban** [cite: 59, 60]

* **Tartalom:** Rámutat, hogy a többnyelvű **korpuszokban** (szöveggyűjteményekben) az adatok minősége nagyon változó lehet. Idéz kutatásokat[cite: 59, 60], amelyek szerint a párhuzamosított (lefordított) adatok jelentős része (akár 20%-a a nyelvek 50%-ánál) pontatlan vagy helytelen lehet[cite: 60].
* **Magyarázat diákoknak:** Még ha vannak is többnyelvű adatok (pl. fordítások), azok minősége gyakran megkérdőjelezhető[cite: 59]. Ha egy modellt rossz minőségű adatokon tanítunk, az maga is rosszul fog teljesíteni. Ezért fontos az adatminőség ellenőrzése és javítása[cite: 60]. A **korpusz** egyszerűen egy nagy szöveggyűjtemény, amit a modellek tanítására használnak.

**23. Dia: Hogyan szerezzünk jobb többnyelvű tanító adatot? (Többnyelvűség)** [cite: 61]

* **Tartalom:** Megvitatja a jó minőségű többnyelvű adatok (pl. **gépi fordításra (MT)** vagy **instrukciókövetésre (instruction tuning)** alkalmas adatok) létrehozásának nehézségét és skálázhatóságát. Megemlít automatikus módszereket (pl. **adatillesztés - alignment**) és **közösségi adatgyűjtési (crowdsourcing)** megközelítéseket[cite: 61].
* **Magyarázat diákoknak:** Hogyan lehetne több és jobb adatot szerezni, különösen az alacsony erőforrású nyelvekhez? Nehéz és drága emberi fordítókat vagy annotátorokat alkalmazni nagy mennyiségben. Ezért keresnek automatikus vagy félautomatikus megoldásokat[cite: 61]. Az **adatillesztés** például megpróbálja automatikusan megtalálni az egymásnak megfelelő mondatokat különböző nyelvű szövegekben. A **közösségi adatgyűjtés (crowdsourcing)** során pedig sok ember kis hozzájárulásával próbálnak adatokat gyűjteni vagy javítani. Az **instrukciókövetés** az, amikor a modellt arra tanítják, hogy kövesse az emberi felhasználó utasításait.

**24. Dia: Értékelés és összehasonlítás** [cite: 62]

* **Tartalom:** Hangsúlyozza, hogy a **benchmarkok** (standardizált tesztek) és az értékelési módszerek alapvetően meghatározzák, hogy a kutatás milyen irányba halad[cite: 62].
* **Magyarázat diákoknak:** Az, hogy mit és hogyan mérünk, nagyban befolyásolja, hogy milyen modelleket fejlesztenek a kutatók. Ha egy **benchmark** (egy standard feladatsor és adathalmaz, amin a modelleket versenyeztetik) például csak a pontosságot méri, a kutatók a pontosság maximalizálására fognak törekedni, még akkor is, ha ez más fontos szempontok (pl. méltányosság, robusztusság) rovására megy. Ezért fontosak a jó értékelési módszerek[cite: 62].

**25. Dia: Chatbotok és nyílt végű rendszerek értékelése (Értékelés)** [cite: 63]

* **Tartalom:** Kiemeli a **nyílt végű rendszerek**, mint a chatbotok értékelésének nehézségét. Tudunk bizonyos problémákról (pl. **hossz biasz** - a modellek hajlamosak hosszabb válaszokat jobbnak értékelni), de sok más rejtett probléma is lehet az értékelési módszereinkben[cite: 63].
* **Magyarázat diákoknak:** Hogyan mérjük meg, hogy egy chatbot "jó"-e? Nincs egyetlen helyes válasz, amit adnia kellene. Ez sokkal nehezebb, mint egy egyszerű osztályozási feladatot értékelni. A jelenlegi módszereknek vannak ismert hibái, például a **hossz biasz** (a modell néha azért kap jobb pontszámot, mert hosszabban válaszol, nem feltétlenül azért, mert jobb a válasz)[cite: 63]. Valószínűleg vannak még más, fel nem ismert problémák is az értékeléssel.

**26. Dia: Mi az arany standard az értékelésben? (Értékelés)** [cite: 64]

* **Tartalom:** Felteszi a nyitott kérdést: mi lenne a legjobb, legmegbízhatóbb ("arany standard") módszer a modellek, különösen a komplexebb, generatív modellek értékelésére[cite: 64]?
* **Magyarázat diákoknak:** Még mindig keressük a tökéletes módszert arra, hogy objektíven és megbízhatóan meg tudjuk mondani, mennyire jó egy NLP modell, különösen a mai modern chatbotok esetében[cite: 64]. Mi lenne az az "arany standard", amihez minden mást mérhetnénk?

**27. Dia: Hogyan őrizzük meg a benchmarkok integritását? (Értékelés)** [cite: 65]

* **Tartalom:** Rávilágít egy problémára: a nagyléptékű előtanítás miatt (ahol a modellek hatalmas mennyiségű internetes szöveget látnak) egyre nehezebb valódi, "rejtett" **tesztadatokat** létrehozni, amelyeket a modell garantáltan nem látott a tanítás során (**adatkontamináció**)[cite: 65].
* **Magyarázat diákoknak:** A modelleket **tesztadatokon** értékeljük, amelyeket elvileg soha nem láttak a tanítás során. De mi van, ha a modell az internet nagy részét "elolvasta" az előtanítás alatt, és a tesztadatok (vagy azokhoz nagyon hasonló adatok) is benne voltak ebben? Ezt hívjuk **adatkontaminációnak**[cite: 65]. Ez torzíthatja az értékelési eredményeket, mert a modell nem általánosít, csak "emlékszik" a válaszra. Egyre nehezebb olyan tesztadatokat találni, amik garantáltan újak a modell számára.

**28. Dia: Hogyan értékeljünk olyasmit, mint az interpretálhatóság? (Értékelés)** [cite: 66]

* **Tartalom:** Felteszi a kérdést, hogyan lehet mérni vagy értékelni a kutatásban egyre fontosabbá váló **kvalitatív** (nem számszerűsíthető) szempontokat, mint például az interpretálhatóságot[cite: 66].
* **Magyarázat diákoknak:** Vannak olyan fontos tulajdonságok, mint a modell működésének érthetősége (interpretálhatóság), amit nehéz egyetlen számmal kifejezni. Hogyan lehet ezeket objektíven értékelni és összehasonlítani különböző modellek között[cite: 66]? Ez is egy nyitott kutatási terület.

**29. Dia: NLP működése nagy hatású területeken** [cite: 67]

* **Tartalom:** Megállapítja, hogy az NLP rendszerek és a **nagy nyelvi modellek (LLM-ek)** a laboratóriumokból kilépve egyre inkább megjelennek a valós világban, olyan nagy hatású területeken, mint a klinikai ellátás, a jog és a tudomány/matematika[cite: 67].
* **Magyarázat diákoknak:** Az NLP már nem csak egyetemi kutatási téma. A technológia eljutott arra a szintre, hogy valós problémák megoldására használják az orvostudományban, a jogi tanácsadásban vagy a tudományos felfedezések segítésében[cite: 67]. Ez óriási lehetőségeket, de felelősséget is jelent. A **nagy nyelvi modell (LLM)** a mai legfejlettebb modellek (mint a ChatGPT alapjául szolgáló GPT modellek) gyűjtőneve.

**30. Dia: Bio / Klinikai NLP (Területek)** [cite: 68]

* **Tartalom:** Részletezi az NLP alkalmazásának lehetőségeit (és kockázatait) az orvostudományban és az alapkutatásban: jegyzetelés segítése, **kérdés-válaszolás (QA)** orvosi szövegekből, "járóbeteg konzultáció" (**curbside consult** - informális segítségnyújtás kollégáknak) támogatása[cite: 68].
* **Magyarázat diákoknak:** Az NLP sokat segíthet az orvosoknak és kutatóknak[cite: 68]. Például automatikusan összefoglalhatná a beteg kórtörténetét, válaszolhatna orvosi kérdésekre szakirodalom alapján, vagy akár segíthetne diagnózisok felállításában (bár itt nagy a felelősség és a kockázat). A **curbside consult** [cite: 68] az, amikor egy orvos gyorsan tanácsot kér egy tapasztaltabb kollégától – ezt is támogathatná egy AI.

**31. Dia: Jogi NLP (Területek)** [cite: 69]

* **Tartalom:** Felveti, hogy az NLP rendszerek segíthetnek áthidalni az "igazságszolgáltatási szakadékot" (**Justice Gap** - azaz, hogy sok ember nem fér hozzá jogi segítséghez), ha képesek megérteni a jogi nyelvezetet és megbízhatóan segíteni a felhasználókat[cite: 69]. Ugyanakkor hangsúlyozza a megbízhatóság és a komplex szakzsargon megértésének szükségességét.
* **Magyarázat diákoknak:** Sok embernek nincs pénze vagy lehetősége ügyvédhez fordulni, még ha szüksége is lenne rá. Ezt nevezik **igazságszolgáltatási szakadéknak (Justice Gap)**[cite: 69]. Az NLP talán segíthetne egyszerűbb jogi kérdések megválaszolásában vagy dokumentumok értelmezésében. De ehhez a modelleknek nagyon megbízhatóknak kell lenniük, és meg kell érteniük a bonyolult, hivatalos jogi nyelvezetet[cite: 69].

**32. Dia: Tudományos NLP (Területek)** [cite: 70]

* **Tartalom:** Említ néhány sikert (pl. a DeepMind FunSearch programja, ami új matematikai megoldásokat talált), de kihívásokat is (pl. a Meta Galactica modellje, ami hibás tudományos szövegeket generált)[cite: 70].
* **Magyarázat diákoknak:** Az NLP a tudományos kutatásban is használható, például új hipotézisek keresésére a szakirodalomban, vagy akár új tudományos eredmények felfedezésére (mint a FunSearch példája)[cite: 70]. De itt is vannak buktatók: a Galactica modell [cite: 70] megmutatta, hogy a modellek magabiztosan állíthatnak valótlanságokat is, ami a tudományban különösen veszélyes.

**33. Dia: Oktatás és NLP (Területek)** [cite: 71]

* **Tartalom:** Megjegyzi, hogy az NLP rendszerek potenciálisan képesek lehetnek megvalósítani a személyre szabott oktatás előnyeit ("Bloom két szigma hatása"), de elismeri, hogy alapjaiban felforgatják a hagyományos oktatást[cite: 71].
* **Magyarázat diákoknak:** **Bloom két szigma problémája** [cite: 71] arra utal, hogy a személyre szabott, egyéni tutorálás sokkal hatékonyabb (átlagosan két szórással jobb eredményt hoz), mint a hagyományos osztálytermi oktatás. Az NLP alapú oktatási eszközök (pl. személyre szabott gyakorló feladatok, azonnali visszajelzés) elméletileg közelebb vihetnek ehhez a hatékonysághoz. Ugyanakkor az olyan eszközök, mint a ChatGPT, komoly kihívások elé állítják az oktatást (pl. hogyan értékeljük a diákok munkáját?)[cite: 71].

**34. Dia: NLP + Más modalitások** [cite: 72]

* **Tartalom:** Bevezeti a **multimodális** NLP fogalmát: a szöveg kombinálása más típusú adatokkal, például képekkel (látás), programkóddal stb. [cite: 72]
* **Magyarázat diákoknak:** Az NLP nemcsak szöveggel foglalkozhat. Mi van, ha egy rendszernek egyszerre kell képet és szöveget értelmeznie (pl. egy kép leírása vagy egy képen látható dologról szóló kérdés megválaszolása)? Vagy ha programkódot kell generálnia egy leírás alapján? Ez a **multimodalitás** területe, ahol a szöveget más típusú információkkal (modalitásokkal) kapcsolják össze[cite: 72].

**35. Dia: Kép-szöveg (Multimodális)** [cite: 73, 74]

* **Tartalom:** Konkrétan a kép-szöveg modellekről beszél (pl. LLaVA, Flamingo)[cite: 73]. Megjegyzi, hogy ezek a modellek már működnek, de talán kevésbé "mély" az integráció a kép és a szöveg között, mint várnánk. Felteszi a kérdést, hogy lehetséges-e mélyebb szintézis, ami nagyobb előrelépést hozna[cite: 74].
* **Magyarázat diákoknak:** Vannak már modellek, amelyek elég jól kezelik a képeket és a szöveget együtt[cite: 73]. De vajon tényleg "értik" a kapcsolatot a kép tartalma és a szöveg között, vagy csak felszínesebb összefüggéseket használnak ki? Lehetséges-e olyan modell, ami valóban egységesen, mélyen integrálja a vizuális és a nyelvi információt[cite: 74]?

**36. Dia: Méltányosság és társadalmi hatás** [cite: 75]

* **Tartalom:** Visszatér a **méltányosság (fairness)** kérdésköréhez. Két fő célt említ: 1) Olyan modellek építése, amelyek méltányosan kezelik az embereket. 2) Kevésbé **sztereotip** reprezentációk létrehozása[cite: 75]. Hangsúlyozza, hogy a modellek valós alkalmazása miatt ezek a szempontok még fontosabbá válnak.
* **Magyarázat diákoknak:** Ahogy ezeket a modelleket egyre több helyen használják, rendkívül fontossá válik, hogy ne legyenek **előítéletesek (biased)** vagy **méltánytalanok** senkivel szemben[cite: 75]. Nem szabad, hogy a modellek káros **sztereotípiákat** erősítsenek meg vagy terjesszenek. Ez nemcsak technikai, hanem etikai kérdés is.

**37. Dia: Előítéletek és sztereotípiák: hogyan mérjük?** [cite: 76]

* **Tartalom:** Említ konkrét **benchmarkokat** (StereoSet, BBQ), amelyeket arra fejlesztettek ki, hogy mérjék a modellekben rejlő sztereotípiákat és előítéleteket[cite: 76].
* **Magyarázat diákoknak:** Ahhoz, hogy csökkenteni tudjuk az előítéleteket a modellekben, először mérni kell tudnunk őket. Vannak erre specializált tesztek (benchmarkok), mint a StereoSet vagy a BBQ[cite: 76], amelyek segítenek feltárni, hogy egy modell hajlamos-e sztereotip kijelentéseket tenni vagy előítéletes következtetéseket levonni.

**38. Dia: Méltányosság és igazságosság: hogyan értékeljük és mérsékeljük?** [cite: 77, 78]

* **Tartalom:** Megvitatja a torzítások értékelését és mérséklését. Példaként említi a **szóvektorokban** felfedezett előítéleteket (pl. bizonyos foglalkozások erősebb társítása egyik nemhez) és az NLP modellek teljesítménybeli különbségeit az alacsony erőforrású nyelvek és **dialektusok** esetében[cite: 77, 78]. Idézi azt a híres tanulmányt, amely kimutatta, hogy a nyelvi korpuszokból automatikusan tanult szemantika emberihez hasonló előítéleteket tartalmaz[cite: 78].
* **Magyarázat diákoknak:** Már a korábbi **szóvektorok** (4. dia) esetében is kimutatták, hogy azok tükrözik a társadalomban meglévő előítéleteket (pl. a 'programozó' szó közelebb volt a 'férfi' szóhoz, mint a 'nő' szóhoz a vektortérben)[cite: 78]. Hasonló problémák vannak a komplexebb modellekkel is, és különösen érintik azokat, akik alacsony erőforrású nyelveket vagy standardtól eltérő **dialektusokat** beszélnek[cite: 77]. A kutatók módszereket fejlesztenek ezeknek a torzításoknak a mérésére és csökkentésére.

**39. Dia: Méltányosság és igazságosság: Mik az LLM-ek nem szándékolt hatásai?** [cite: 79, 80, 81]

* **Tartalom:** Bemutat egy példát az LLM-ek **nem szándékolt hatásaira**. Egy LLM **jutalom modellje** (ami azt tanulja meg, hogy milyen válaszok "jók") magasabb jutalmat adott a modellnek, ha azt mondta, hogy egy angolszász, nyugati országból származik, és alacsonyabbat, ha közel-keleti vagy afrikai országból[cite: 79, 80]. Ez azt jelzi, hogy a modell **illesztése (alignment)** során (amikor megpróbálják biztonságosabbá és segítőkészebbé tenni) akaratlanul is bevihetők vagy felerősíthetők bizonyos földrajzi vagy kulturális torzítások[cite: 81].
* **Magyarázat diákoknak:** Amikor a fejlesztők megpróbálják "jó viselkedésre" tanítani a nagy nyelvi modelleket (ezt hívják **illesztésnek - alignment**), néha akaratlanul is újabb problémákat okozhatnak[cite: 81]. Ebben a példában [cite: 79, 80] a modell megtanulta, hogy "jobb" válasz nyugati országból származni, ami nyilvánvalóan egy elfogult és nem kívánatos viselkedés. Ez mutatja, hogy nagyon óvatosnak kell lenni a modellek finomhangolásával. A **jutalom modell** az illesztési folyamat része, ami megmondja, hogy a modell válaszai mennyire felelnek meg az elvárásoknak.

**40. Dia: Az NLP társadalmi aspektusai** [cite: 82]

* **Tartalom:** Felsorol további társadalmi szempontokat, amelyek fontosak az NLP-ben: Kultúra és Vallás, Társadalmi Normák, Alulreprezentált Csoportok[cite: 82].
* **Magyarázat diákoknak:** Az NLP fejlesztésekor nemcsak a technikai pontosságra kell figyelni, hanem arra is, hogyan hat a technológia a különböző kultúrákra, vallásokra, hogyan kezeli a társadalmi normákat, és hogyan érinti azokat a csoportokat, akik eddig kevesebb figyelmet kaptak a digitális világban[cite: 82].

**41. Dia: Az NLP társadalmi aspektusai** [cite: 83, 84]

* **Tartalom:** Hangsúlyozza a társadalmi tudatosság köré épülő kutatási kérdések és technikák kidolgozásának szükségességét[cite: 83]. Figyelembe kell venni: a beszélőket, az alacsony erőforrású nyelveket és dialektusokat, a sérülékeny csoportokat, a kultúrát és ideológiát (Kinek az értékei jelennek meg?), valamint a normákat és kontextust (Mikor és hol elfogadható egy adott viselkedés?)[cite: 84]. Hivatkozik Hovy és Yang 2021-es cikkére[cite: 84].
* **Magyarázat diákoknak:** Aktívan kell kutatni, hogyan lehet az NLP-t társadalmilag érzékenyebbé tenni[cite: 83]. Figyelembe kell venni a felhasználók hátterét, nyelvét, kultúráját, és azt, hogy a modell viselkedése különböző helyzetekben (kontextusokban) hogyan hat[cite: 84]. Kinek az értékeit tükrözi a modell? Hogyan lehet biztosítani, hogy ne sértse meg a társadalmi normákat?

**42. Dia: Implicit tudás NLP modellekben: józan ész** [cite: 85]

* **Tartalom:** Foglalkozik az **implicit tudás** és a **józan ész (commonsense)** modellezésének kihívásával. Ez magában foglalja az időbeli, fizikai, társadalmi összefüggések megértését és a "tudatelmélet" (**theory of mind** - mások mentális állapotainak tulajdonítása) képességét[cite: 85]. Hivatkozik kapcsolódó kutatásokra (Bosselut et al., 2019; Sap et al., 2022)[cite: 85].
* **Magyarázat diákoknak:** Az emberek rengeteg olyan tudással rendelkeznek a világról, amit magától értetődőnek vesznek – ez a **józan ész**. Például tudjuk, hogy a víz nedves, hogy az emberek általában nem repülnek, vagy hogy ha valaki sír, valószínűleg szomorú. Ezt az **implicit tudást** nagyon nehéz a gépeknek megtanítani. A **"theory of mind"** [cite: 85] az a képességünk, hogy megértsük, másoknak is vannak gondolatai, szándékai, érzései, amelyek eltérhetnek a mieinktől. Ennek modellezése is nagy kihívás az AI számára.

**43. Dia: Fenntarthatóság és energia (Hatás)** [cite: 86]

* **Tartalom:** Felveti a nagy NLP rendszerek magas energiafogyasztásának problémáját és a hatékonyabbá tétel szükségességét (**fenntarthatóság**)[cite: 86].
* **Magyarázat diákoknak:** A nagy nyelvi modellek tanítása és futtatása rengeteg energiát igényel, ami jelentős környezeti terheléssel jár[cite: 86]. Fontos kutatási irány, hogyan lehetne ezeket a modelleket **hatékonyabbá**, "zöldebbé" tenni, hogy csökkentsük az ökológiai lábnyomukat (**fenntarthatóság az AI-ban**).

**44. Dia: Összegzés** [cite: 87, 88, 89, 90]

* **Tartalom:** Lezárja az előadást. Megköszöni a figyelmet[cite: 87], összefoglalja a legfontosabb tanult ötleteket (disztribucionális reprezentációk, NN-alapú NLP rendszerek építése, előtanítás, adaptáció)[cite: 88], kiemeli a nagy lehetőségeket a valós alkalmazásokban[cite: 89], és emlékeztet a megmaradt nyitott kérdésekre (pl. általánosítás, értékelés)[cite: 90]. Izgalmas időszaknak nevezi a terület jelenlegi helyzetét[cite: 90].
* **Magyarázat diákoknak:** Ez az utolsó dia összefoglalja, miről volt szó. Felidéztük a legfontosabb technikákat, amik a mai NLP alapját képezik[cite: 88]. Láttuk, hogy ezek a technológiák már képesek valódi problémákat megoldani[cite: 89], de azt is, hogy rengeteg még a megoldatlan kérdés és a kihívás, például a modellek megbízható általánosítása vagy a korrekt értékelésük[cite: 90]. Ez egy nagyon gyorsan fejlődő, izgalmas terület[cite: 90].