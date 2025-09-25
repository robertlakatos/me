collection: teaching
type: "B.Sc course"
permalink: materials/AIPD/labor/II-theoretical-background
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-09-25
location: "Debrecen, Hungary"
---

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