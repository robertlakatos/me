---
title: "Introduction to AI and Decision Making"
collection: teaching
type: "M.Sc course"
permalink: materials/AIPD/labor/IV-pe-advanced
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-10-09
location: "Debrecen, Hungary"
---

# Prompt Engineering - Advanced

- [Instruction-tuning](https://robertlakatos.github.io/me/materials/NLP-A/lectures/instruction-tuning-rlhf.pdf)
- [How to work - Google AI studio](https://aistudio.google.com/)

## English

### Task 1.

```Prompt
Imagine a bakery with 12 dozen buns. During the morning, they sold 87 buns. At noon, they baked 3 dozen more buns. Then, they put all the remaining buns into 3 equal piles. How many buns are in each pile?
```

### Task 2.

```Prompt
Anna, Bence, and Csaba went to a café and each ordered a drink: coffee, tea, and hot chocolate. Each of them has a different job: teacher, engineer, and chef.
- The one who is an engineer ordered coffee.
- Bence is not the teacher.
- Csaba is the chef.
- The one who ordered hot chocolate is not the engineer.

Question: Who is the teacher, and what did Bence order?
```

### Why are these tasks suitable for demonstrating CoT?
- Linking Multiple Variables: The solution requires linking the name, occupation, and drink.
- Step-by-Step Inference: Cannot be solved immediately; the model must use one piece of information to rule out or confirm the next.
- Exclusionary Logic: CoT is ideal for demonstrating exclusionary logic (like points 2 and 4).

## Magyar

### Feladat 1:

```Prompt
Képzelj el egy pékséget, ahol van 12 tucat zsemle. A délelőtt folyamán eladtak 87 zsemlét. Délben sütöttek még 3 tucat zsemlét. Ezután az összes megmaradt zsemlét 3 egyenlő kupacba rakták. Hány zsemle van minden kupacban?
```

### Feladat 2:

```Prompt
Anna, Bence, és Csaba elmentek egy kávézóba, és mindannyian rendeltek egy italt: kávét, teát, és forró csokoládét. Mindegyikük más foglalkozást űz: tanár, mérnök, és séf.
- Aki mérnök rendelt kávét.
- Bence nem a tanár.
- Csaba a séf.
- Aki rendelt forró csokoládét nem a mérnök.

Kérdés: Ki a tanár, és mit rendelt Bence?
```

### Miért jók ezek a feladatok a CoT bemutatására?
- Több Változó Összekapcsolása: A megoldáshoz a nevet, a foglalkozást és az italt kell összekapcsolni.
- Lépésről Lépésre Következtetés: Nem lehet azonnal megoldani; a modellnek az egyik információt kell felhasználnia a következő kizárásához vagy megerősítéséhez.
- Kizárásos Logika: A CoT ideális a kizárásos logika (mint a 2. és 4. pont) megjelenítéséhez.

