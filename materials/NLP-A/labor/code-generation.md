---
title: "Code Generation"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/code-generation
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-05-06
location: "Debrecen, Hungary"
---

## [Colab](https://drive.google.com/file/d/1n-wZxG5wbCBeI2iB2Af6zS4bZd8kXNbr)

## Bevezetés | Introduction:

**Magyar:** Ez a feladat a Google Colab interaktív környezetét és a benne elérhető beépített kódgeneráló funkciót használja a programozási problémák megoldására. A cél nem csupán a működő kód megszerzése, hanem a generált kód minőségének kritikus értékelése, a generálási folyamat megértése, és annak dokumentálása, hogy a promptok hogyan befolyásolják az eredményt. Kiemelten fontos a generált kód validálása tesztek vagy vizualizációk segítségével.

**English:** This assignment utilizes the interactive environment of Google Colab and its built-in code generation feature to solve programming problems. The goal is not merely to obtain working code, but to critically evaluate the quality of the generated code, understand the generation process, and document how prompts influence the outcome. Validating the generated code using tests or visualizations is of particular importance.

### Hogyan használd a Colab kódgenerálóját | How to use Colab's Code Generator:

**Magyar:** A Colab legújabb verzióiban a kódcellák mellett vagy egy külön menüpontban (keresd a "Help me code" vagy hasonló gombot/opciót) találsz lehetőséget arra, hogy a beírt természetes nyelvi leírás alapján kódot generáltass. Kísérletezz vele, hogyan tudod a leghatékonyabban használni!

**English:** In the latest versions of Colab, you will find an option next to the code cells or in a separate menu (look for the "Help me code" or similar button/option) that allows you to generate code based on your natural language description. Experiment with how you can use it most effectively!

### Feladatok | Tasks:

**Magyar:** Az alábbiakban 15+ programozási feladat található, különböző területekről. Minden feladat esetén a következő lépéseket kell elvégezned a Colab notebookban: prompt megfogalmazása, kód generálása, tesztelés (manuális és unit tesztekkel) és/vagy vizualizáció, értékelés és elemzés, dokumentálás.

**English:** Below are 15+ programming tasks from various domains. For each task, you need to perform the following steps in the Colab notebook: formulate the prompt(s), generate the code, test (manually and with unit tests) and/or visualize, evaluate and analyze, and document.

### Validálás | Validation:

- Unit tesztek: Kisebb, jól definiálható bemenettel rendelkező funkciók esetén írj unit teszteket a unittest vagy pytest segítségével. Teszteld a szokásos eseteket, sarok eseteket és a hibakezelést.
- Vizualizáció: Adatmanipulációs, statisztikai vagy gépi tanulási feladatok esetén használj vizualizációs eszközöket (pl. Matplotlib, Seaborn) a generált kód viselkedésének, az adatok eloszlásának, a modell teljesítményének vagy az eredmények ellenőrzésére.

- Unit Tests: For smaller functions with well-defined inputs, write unit tests using unittest or pytest. Test standard cases, edge cases, and error handling.
- Visualization: For data manipulation, statistical, or machine learning tasks, use visualization tools (e.g., Matplotlib, Seaborn) to verify the behavior of the generated code, data distribution, model performance, or results.