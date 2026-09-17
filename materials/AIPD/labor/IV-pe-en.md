---
title: "Introduction to AI and Decision Making"
collection: teaching
type: "M.Sc course"
permalink: materials/AIPD/labor/IV-pe-en
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2026-09-16
location: "Debrecen, Hungary"
---

# Prompt Engineering

# Practical Prompt Engineering with Gemini

This lab exercise introduces techniques for effective communication with Large Language Models (LLMs)—specifically, prompt engineering. The goal is to enable you to use artificial intelligence not merely as a search engine, but as a programmable cognitive assistant.

## 1. In-context learning

One of the most important characteristics of language models is **in-context learning**. This means the model is capable of learning and applying new patterns, rules, or tasks *based solely on the information provided in the prompt*, without the need to retrain its internal (structural) weights. If you introduce a new framework within the conversation, the model adapts to it immediately.

> **Demonstration example:**
> *User:* "In our internal company jargon, a 'Blue Penguin' refers to a customer who asks a lot of questions but never makes a purchase. A 'Red Leopard,' on the other hand, is someone who pays immediately without asking questions. With this in mind, analyze the following sales report: 'A guy came in today, grilled me about the warranty for an hour, and then left. Afterward, a lady came in, pointed to the most expensive machine, and paid with her bank card.'"
> *Model response:* "The first customer was a typical Blue Penguin, while the second was clearly a Red Leopard." ## 2. Zero-shot learning

In **Zero-shot learning**, we ask the model to solve a task without providing any prior examples in the prompt. In this scenario, the model relies solely on the vast, general knowledge base it acquired during training to interpret the task.

> **Example:** "Classify the following customer review (Positive, Negative, Neutral): *The software interface is clear, but the data export function is very slow.*"

* **Student task in Gemini:**
Give Gemini a zero-shot prompt asking it to write a professional, 3-line rejection email to a job applicant. Do not provide a template or example; let it generate the format itself. Try running it multiple times by starting new chat windows and observe the differences.

## 3. Few-shot learning

If zero-shot learning does not yield sufficiently accurate results, or if a very specific output format is required, we use **few-shot learning**. In this case, we provide 2–3 (or more) concrete examples of input-output pairs within the prompt, allowing the model to learn the logic and format we expect.

> **Example:**
> Convert the raw product names into our webshop's category system! > Raw: iPhone 14 Pro -> Category: Smartphones
> Raw: LG 55-inch 4K -> Category: Televisions
> Raw: Bosch food processor -> Category: Kitchen appliances
> Raw: Samsung Galaxy S23 -> Category: ?

* **Student task in Gemini:**
You have a list of unstructured addresses (e.g., "Budapest kossuth Lajos utca 12 1053", "Szeged, 6720 Kárász u. kilenc"). Create a few-shot prompt with 3 examples that teaches Gemini to convert the raw input addresses into exactly this JSON format: `{"PostalCode": "...", "City": "...", "Street_HouseNumber": "..."}`. Test it with a new address!

## 4. System prompt

The **System prompt** defines the language model's "personality," behavioral rules, and limitations at the very beginning of the conversation. It serves as the background instruction based on which the AI ​​interprets subsequent standard user queries. (In Gemini, you can simulate this by strictly defining the model's role—i.e., its persona—in your first message.)

**Important:** Large systems operate using their own system prompts; while you can refine this with a persona, you cannot overwrite the underlying system prompt itself. > **Example:**
> "From this moment on, you are a strict, data-driven risk analyst. Whatever business idea I describe, your response must always focus on the worst-case scenario and financial risks. Never be overly optimistic. Keep your answers brief and objective."

## 5. Rhetorical Prompt Engineering

Rhetorical prompt engineering involves applying techniques from human communication (such as personas, argumentation structures, and defining the target audience). We don't just tell the machine *what* to do, but also *for whom*, *in what style*, and *with what intent*. This allows us to fine-tune the nuances of the response.

> **Examples:**
> * "Explain how neural networks work to a 10-year-old child, using language they would understand."
> * "Argue that cloud-based data storage is dangerous, adopting the persona of a leading 1990s cybersecurity expert who is suspicious of new technologies."
>
>

* **Student tasks in Gemini:**
1. Ask Gemini to explain the difference between correlation and causation (cause and effect) to a skeptical executive who is about to fire an entire department due to a misleading statistic.
2. Ask for a brief explanation of a piece of Python code, but phrase the instruction like this: "Explain this line of code as if you were Gordon Ramsay and my code was full of amateur mistakes."

## 6. Meta-prompting

**Meta-prompting** is when we use a language model to create, evaluate, or improve prompts *itself*. Instead of having it solve the final task, we automate the process of formulating better questions.

* **Student exercises for Gemini:**
1. Enter this into Gemini: *"I want to build a machine learning model in Python that predicts customer churn. Write three perfect, detailed prompts for me; if I feed them back to you later, you should be able to provide the best possible assistance and code outline for the job."*
2. Write a very poor, incomplete prompt for Gemini (e.g., *"make a table with data"*). Immediately afterwards, ask it: *"Critique my previous prompt! Tell me what is missing and rewrite it so it looks like a prompt from a professional data analyst!"*

## 7. Extra prompting techniques

* **Chain-of-Thought (Step-by-step reasoning):** We force the model to lay out its logical steps before providing the final answer. This drastically reduces hallucinations in mathematical or logical tasks. * **Task:** Ask a complex logic puzzle (e.g., "If 5 machines produce 5 products in 5 minutes, how long does it take for 100 machines to produce 100 products?") and add: *"Before giving the final answer, work through the solution step-by-step, thinking out loud."*

* **Constraint Prompting (Strict constraints):** Locking in the output format.
* **Task:** Ask for 3 business ideas for student jobs, but specify: *"Your answer must be EXCLUSIVELY a Markdown table with 3 columns (Idea, Cost, Time Requirement). You may not include introductory text or a conclusion below the table. Return only the table itself."*

### 8. Iterative Prompting (Step-by-step fine-tuning)

Prompt engineering rarely involves a single, magically perfect question. Attempting to solve complex, multifaceted problems "in one go" (requesting everything in one massive prompt) often yields superficial, illogical, or erroneous (hallucinated) results. The most effective way to work with language models is through iteration: breaking the task down into smaller logical steps, continuously checking the machine's output, and refining the direction based on the responses received. This not only makes the result more reliable but also allows for fine-tuning details along the way. * **Example (All-at-once vs. Iterative):** Poor approach (All-at-once): "Write a complete business plan for a vegan bakery in Budapest; include a financial plan, marketing strategy, competitor analysis, and a weekly social media calendar." (The result will likely be a very generic, cliché-ridden, superficial document with undeveloped figures).

* **Good approach (Iterative):**
Step 1: "I want to open a vegan bakery in Budapest. Write 3 unique selling propositions (USPs) that would help me stand out in the market." (Result: The model provides 3 ideas).
Step 2: "I like idea #2 the best (sugar-free baked goods for athletes). Create a detailed target audience profile for this concept." (Result: A targeted, relevant profile).
Step 3: "Great. Based on this target audience, write a 5-day Instagram content calendar focused on them." (Result: A highly specific, high-quality, and coherent outcome, built step-by-step).

* **Student task in Gemini:**
Try out the power of iteration on a data analysis (coding) problem! Do not ask for a complete, finished program all at once. Proceed according to the following steps, and wait for the AI's response at each stage:
**1. **Prompt:** "Write me some Python (Pandas) code that loads a file named 'sales_data.csv' and prints the number of missing values ​​(NaNs) in each column to the screen."
**2. Prompt (After the response):** "Let's assume missing values ​​were found in the 'Arbevetel' column. Modify the previous code to fill these missing values ​​with the column's median!"
**3. Prompt (After the response):** "Perfect. Now add a Seaborn plot to the code that visualizes the distribution (histogram) of the cleaned 'Arbevetel' column. The plot should have a title and axis labels in Hungarian."

(Notice how much easier it is to verify the machine's work this way—and to make corrections if it misinterpreted something the first time!)

---

## Conclusion: The Future of Language Models and Communication

The way language models operate points to a fundamental paradigm shift in computing: **natural language has become the new programming language.** When you converse with Gemini (or another model), you aren't actually "chatting." You are configuring a high-performance supercomputer that has learned to recognize patterns within massive datasets.

The key insight of Prompt Engineering is that the quality of the model's output matches the quality of the instruction (Garbage In, Garbage Out). These systems represent universal communicatact as an interface between human and machine, where our words serve as the control codes.

## Complete the following quiz [link](https://share.gemini.google/e5vzEai75fxt)

## Concluding Reflection (For your project assignment)

Reflect on your own business AI project from this semester.

* How can you apply the techniques mentioned above when performing Exploratory Data Analysis (EDA) in Google Colab?
* Which technique would best help ensure that the model not only generates code but also explains the workings of the decision tree to a manager?
* Plan out—mentally or in a rough sketch on paper—the System Prompt you would set for the AI ​​to ensure it acts as the best possible technical mentor for your project!

---
