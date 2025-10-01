---
title: "Introduction to AI and Decision Making"
collection: teaching
type: "M.Sc course"
permalink: materials/AIPD/labor/III-pe-base
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-10-01
location: "Debrecen, Hungary"
---

# Prompt Engineering - Base

## English

## Definition of Prompt Engineering (PE):

The technique of optimizing input instructions (**prompts**) to obtain the most accurate and relevant output from a generative AI system. This is the art and science of "talking" to the AI.

## The Core "Pillars" of a Prompt

Every effective prompt should contain the following elements (or at least strive to):
- **Context:** Any background information that helps the model answer. (Example: "We are in a 20th-century literature course.")
- **Task:** The specific goal to be achieved. (Example: "Summarize the 5 main plot twists of **Hamlet**.")
- **Persona/Format:** The model's behavior and the desired structure of the output. (Example: "Act as a high school teacher. The output should be a bullet point list.")
- **Iteration:** Prompt engineering is not a one-time attempt. Continuous refinement of the prompt is necessary for better results.

## Practical Exercises on the Gemini Interface:
- Testing the Impact of Context:
    - **Prompt (Without Context):** "What is the function of money?"
    - **Prompt (With Context):** "In the context of **medieval Europe**, where bartering dominates, what is the **primary** function of money?"
    - **Goal:** Compare how the answer changes when the context is provided.
- Refining the Task: Find a simple recipe (e.g., scrambled eggs).
    - **Prompt (General Task):** "How do you make scrambled eggs?"
    - **Prompt (Specific Task):** "How do you make the **fluffiest, creamiest** scrambled eggs in **three minutes**, according to the secret method of **French chefs**?"
    - **Goal:** Demonstrate how a specific task leads to much more relevant, in-depth content.

## The Basic "Anatomy": Structuring the Prompt

This section equips students with the practical linguistic tools to immediately improve the effectiveness of their prompts.

- Clear and Specific Instructions: Avoid subjective words, and all parameters must be quantified/specified. (Example: "Don't write a *good* summary, write a **250-word** summary in **three points**.")
- Role-Playing / Persona: Assigning a "personality" or expertise to the model at the beginning of the prompt. This ensures the appropriate tone and subject matter knowledge. (Example: "Act as a critical film reviewer.")
- Constraints: Precise restrictions on the output's form and content. This includes **format** (JSON, Markdown table, bullet points), **tone** (Formal, Friendly), and **length** (Max. 10 sentences).

## Practical Exercises (Gemini Interface & Google Colab):

1. Persona and Tone Switching
- **Technique:** Persona
- **Task:** Choose one of the following topics: Prompt Engineering, The history of coffee, The latest scientific breakthrough.
- **Prompts:**
    - Ask Gemini to explain the topic in the tone of a **determined, motivational trainer**.
    - Ask it to explain the same topic in the tone of a **sleepy, cynical librarian**.
- **Goal:** To feel the power of **Persona** to dramatically change the tone and style of the output.
2. Structured Data Request in JSON Format (Google Colab - Python API)
- **Technique:** Constraints (Format)
- **Task:** Request machine-readable, structured data from the model.
- **Prompt:** Ask the model to generate the names of 5 popular programming languages. In the prompt, request that the output be a standard, **validatable JSON format list** that includes the language name and its primary use case.
- **Goal:** To demonstrate the importance of machine-readable **Format Constraints** (e.g., JSON) in automated processes and API usage.
3. Length and Format Constraints (Gemini Interface)
- **Technique:** Specific Instructions, Constraints (Length, Format, Vocabulary)
- **Task:** Request a comparison between Mars and Venus.
- **Prompt:** In the prompt, specify the following:
    - Use only simple words,
    - The answer should be a bulleted list with 4 points,
    - The total answer must be a maximum of 35 words.
- **Goal:** To practice enforcing strict **Constraints** regarding content (vocabulary), length, and format.

## Magyar

## Prompt Engineering (PE) Defíníciója: 

Az a technika, amellyel a bemeneti utasításokat (promptokat) optimalizáljuk, hogy a generatív MI rendszertől a legpontosabb és legrelevánsabb kimenetet kapjuk. Ez a "beszélgetés" művészete és tudománya az MI-vel.

## A Prompt Alapvető "Pillére"

Minden hatékony promptnak tartalmaznia kell a következő elemeket (vagy legalábbis célszerű):
- **Context (Környezet):** Minden háttérinformáció, ami segít a modellnek a válaszadáshoz. (Példa: "Egy 20. századi irodalmi kurzuson vagyunk.")
- **Task (Feladat):** A konkrét cél, amit el kell érni. (Példa: "Foglalja össze a Hamlet 5 fő cselekményfordulatát.")
- **Persona/Format (Szerep/Formátum):** A modell viselkedése és a kimenet kívánt struktúrája. (Példa: "Tegyél úgy, mint egy középiskolai tanár. A kimenet egy bullet point lista legyen.")
- **Iteráció:** A prompt engineering nem egyszeri próbálkozás. Szükség van a prompt folyamatos finomítására a jobb eredmény érdekében.

## Gyakorlati Feladatok a Gemini Felületén:
- Környezet (Context) Hatásának Vizsgálata:
    - **Prompt (Context Nélkül):** "Mi a pénz funkciója?"
    - **Prompt (Context-tal):** "A középkori Európa kontextusában, hol a cserekereskedelem dominál, mi a pénz elsődleges funkciója?"
    - **Cél:** Hasonlítsátok össze, hogyan változik a válasz, ha a környezetet megadjuk.
- Feladat (Task) Finomítása: Keressetek egy egyszerű receptet (pl. rántotta).
    - **Prompt (Általános Task):** "Hogyan kell rántottát csinálni?"
    - **Prompt (Specifikus Task):** "Hogyan kell a legbolyhosabb, legkrémesebb rántottát elkészíteni három perc alatt, a francia séfek titkos módszere szerint?"
    - **Cél:** Bemutatni, hogy a specifikus feladat (Task) hogyan vezet sokkal relevánsabb, mélyebb tartalomhoz.

## Az Alapvető "Anatómia": A Prompt Felépítése

Ez a szakasz a gyakorlati nyelvi eszközöket adja a hallgatók kezébe, amelyekkel azonnal javíthatják a promptjaik hatékonyságát.

- Világos és Konkrét Utasítások: Kerülni kell a szubjektív szavakat, és minden paramétert számszerűsíteni/specifikálni kell. (Példa: "Ne jó összefoglalót írj, hanem 250 szavas összefoglalót három pontban.")
- Szerepjáték / Persona (Role-Playing): A modell "személyisége" vagy szakértelme megadása a prompt elején. Ez biztosítja a megfelelő hangnemet és szaktudást. (Példa: "Tegyél úgy, mint egy kritikus filmkritikus.")
- Korlátok (Constraints): Pontos megkötések a kimenet formájára és tartalmára vonatkozóan. Ide tartozik a formátum (JSON, Markdown táblázat, Felsorolás), a hangnem (Hivatalos, Barátságos), és a hossz (Max. 10 mondat).

## Gyakorlati Feladatok a Gemini Felületén:

1. Persona és Hangnem Váltás
- **Technika:** Persona
- **Feladat:** Válassz egyet az alábbi témák közül: Prompt Engineering, A kávé története, A legújabb tudományos áttörés.
- **Promptok:**
    - Kérd meg a Geminit, hogy magyarázza el a témát egy határozott, motivációs tréner hangján.
    - Kérd meg, hogy magyarázza el ugyanazt a témát egy álmos, cinikus könyvtáros hangján.
- **Cél:** Érzékelni a Persona erejét, amivel drámaian megváltoztatható a kimenet hangneme és stílusa.
2. Strukturált Adatkérés JSON Formátumban (Google Colab - Python API)
- **Technika:** Korlátok (Formátum)
- **Feladat:** Kérj a modelltől géppel olvasható, strukturált adatot
- **Prompt:** Kérd meg a modellt, hogy generáljon 5 népszerű programozási nyelv nevét. A promptban kérd, hogy a kimenet egy standard, érvényesíthető JSON formátumú lista legyen, amelyik tartalmazza a nyelv nevét és a fő felhasználási területét.
- **Cél:** Bemutatni, hogy a géppel olvasható Formátum Korlátok (pl. JSON) mennyire fontosak az automatizált folyamatokban és az API használatban.
3. Hossz és Formátum Korlátok (Gemini Felület)
- **Technika:** Konkrét Utasítások, Korlátok (Hossz, Formátum, Szókincs)
- **Feladat:** Kérj egy összehasonlítást a Mars és a Vénusz között.
- **Prompt:** A promptban határozd meg a következőket: 
    - Használjon csak egyszerű szavakat, 
    - A válasz pontokba szedett lista legyen 4 pontból, 
    - Maximum 35 szó legyen a teljes válasz.
- **Cél:** Gyakorolni a szigorú Korlátok betartatását a tartalom (szókincs), a hossz és a formátum tekintetében.