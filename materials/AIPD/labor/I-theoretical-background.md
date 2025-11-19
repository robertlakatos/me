collection: teaching
type: "B.Sc course"
permalink: materials/AIPD/labor/I-theoretical-background
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-09-25
location: "Debrecen, Hungary"
---

## The basics of decision making (A döntéshozatal alapjai)

### 1. Problem identification: The first step is always to define the problem or opportunity precisely. What do we want to achieve or change? (Probléma azonosítása: Az első lépés mindig a probléma vagy lehetőség pontos meghatározása. Mi az, amit el szeretnénk érni vagy megváltoztatni?)

### 2. Gathering information: Gathering all the relevant information needed to make a decision. This may include analyzing data, seeking expert opinions, or relying on our own experience. (Információ gyűjtés: A döntéshez szükséges összes releváns információ összegyűjtése. Ez magában foglalhatja adatok elemzését, szakértői vélemények kikérését, vagy saját tapasztalatainkra támaszkodást.)

### 3. Generating alternatives: Developing several possible solutions or alternatives. The more options we explore, the more likely we are to make the best decision. (Alternatívák generálása: Több lehetséges megoldás vagy alternatíva kidolgozása. Minél több lehetőséget vizsgálunk meg, annál valószínűbb, hogy a legjobb döntést hozzuk.)

### 4. Evaluating alternatives: Comparing the advantages and disadvantages of alternatives. To do this, we can evaluate options based on various aspects, such as costs, time, risks, and benefits. (Alternatívák értékelése: Az alternatívák előnyeinek és hátrányainak összehasonlítása. Ehhez különböző szempontok alapján értékelhetjük a lehetőségeket, például a költségeket, az időt, a kockázatokat és az előnyöket.)

### 5. Making a decision: Choosing the best alternative. It can be a rational decision based on data and logic or an intuitive decision that relies more on feelings and experience. (Döntés meghozatala: A legjobbnak ítélt alternatíva kiválasztása. Ez lehet egy racionális döntés, amely adatokon és logikán alapul, vagy egy intuitív döntés, amely inkább érzésekre és tapasztalatokra támaszkodik.)

### 6. Decision implementation: Implementation of the selected alternative. This may include defining specific steps, providing resources, and delegating tasks. (Döntés végrehajtása: A kiválasztott alternatíva megvalósítása. Ez magában foglalhatja konkrét lépések meghatározását, erőforrások biztosítását és a feladatok delegálását.)

## How and why does it work?

- Complex system / Agent approach
- Generative model
- Large language model
- Transformer architecture
- Neural network
- Cosine similarity
- Embedded vectors

## What is a pattern recognition system?

## Practice (using Google Gemini/Colab)

### 1. Exercise Steps:

A. Sample-Teach (Simulating Fine-Tuning)

Phase: Introductory, "teaching" phase.

Create a Handmade (Artificial) Sample:
Ask students to give Gemini a set of input-output pairs that contain an artificial grammar sample.

```Prompt 
You can see a pattern in the following 4 examples. Notice the relationship between the input and the output:
Input: Football, Sport
Output: Football, Exercise
Input: HTML, Code
Output: HyperText Markup Language, Programming
Input: Budapest, Capital
Output: Hungary, Public Administration
Input: Acceleration, Force
Output: Physics, Motion
```

```Prompt
You can see a pattern in the following 4 examples. Notice the relationship between the input and the output:
Input: Football, Sport
Output: Football, Exercise
Input: HTML, Code
Output: HyperText Markup Language, Programming
Input: Budapest, Capital
Output: Hungary, Public Administration
Input: Acceleration, Force
Output: Physics, Motion

Now, identify this pattern and apply it to the following input: Demand, Market
```

Observation: Students should observe that the model is expected to try to copy the pattern (Input: technical term, category; Output: explanatory term, broader area).

### 2. Exercise Steps

```Prompt
Knowing the above pattern, what will be the output for the following input: Baking paper, Horse
```