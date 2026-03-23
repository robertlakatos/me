---
title: "Advanced Natural Language Processing"
collection: teaching
type: "M.Sc course"
permalink: /teaching/NLP-A
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-02-09
location: "Debrecen, Hungary"
---

This course delves into advanced concepts of Natural Language Processing (NLP) and Machine Learning (ML) with a strong focus on modern deep learning techniques. It covers foundational topics such as tokenization, text representation, and pipelines, as well as cutting-edge research in large language models (LLMs), transformers, and their applications. The course emphasizes both theoretical understanding and practical implementation, preparing students to tackle real-world NLP challenges, including security, privacy, and human-centered design. During the semester, students will also have the opportunity to test and train these architectures on real data using cloud-based services [(Google Collab)](https://colab.google/).

======

## [Email address of the Teacher](mailto:lakatos.robert@inf.unideb.hu)

## Consultation

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

## [Attendance sheet](https://forms.cloud.microsoft/e/Ek0iSB0fjC?origin=lprLink)

## [Attendance sheet status](https://unidebhu-my.sharepoint.com/:x:/g/personal/lakatos_robert_inf_unideb_hu/IQCCnu6AtHk1TpCV4NsYwGVqASFjuU1MguAOZNI0A8oSHlY?e=B3IZ3O)

## Requirements

### Project Overview

The goal of this assignment is to design, implement, and evaluate a Multi-Agent System (MAS) using Large Language Models (LLMs). Instead of relying on a single "monolithic" chat prompt, you must decompose a complex problem into specific sub-tasks handled by at least two distinct agents.

A key part of this project is understanding the transition from "Prompt Engineering" to "Agentic Workflows." You will demonstrate how specialized roles, even when powered by the same local model, can produce superior results compared to a single-agent baseline.

### Core Requirements

- Attendance sheet: Fewer absences than allowed. Active participation in classes.
- Create a working application, solve a real problem, and present it as a video using the solutions and models learned in class.
     - Maximum length of video is 5-10 minutes.
     - In the video, each creator must present their own contribution. (for 3-8 minutes)
     - The application must be shown in action at the end of the video. (for 1-2 minutes)
     - Video size must be 50 MB or less.
     - The group members (students) have to send one and clear (without executed blocks) Jupyter notebook (ipynb) file with Python code that contains all the project code.
     - **Local Execution:** All agents must run locally using Ollama.
     - **Multi-Agent Design:** Use at least two agents with unique system instructions (e.g., a Researcher and a Technical Writer, or a Coder and a Reviewer).
     - **Comparative Analysis:** You must compare the multi-agent output against a "Baseline" (a single prompt sent to a standard chat agent).
- Organizing into teams (2-4 people) or working individually.
- It is not certain that the team members receive a uniform grade, but they get grades proportionate to the task they have completed in the project.

### Evaluation

Grade | Requirements
--- | --- | ---
5 (Excellent)	| Outstanding original idea. Robust orchestration (e.g., iterative feedback loops between agents). Deep theoretical understanding of parameters (temperature, context window) and clear proof that the multi-agent approach significantly outperformed the baseline.
4 (Good)	| Complex interaction logic. Agents provide critical feedback to one another. Detailed comparison with the baseline using specific metrics (e.g., accuracy, code quality, or hallucination reduction).
3 (Fair) | Practitioner	Clearly defined roles with distinct System Prompts. The notebook is well-documented and the comparison between the "single chat" and "multi-agent" results is present.
2 (Pass) | Basic implementation of two agents (e.g., Writer + Editor). The code runs on Ollama, but agent differentiation is minimal. The video explains the "how" but struggles with the "why" regarding agentic workflows.
1 (Fail) | The system does not run locally, uses only one agent, or lacks the required video/notebook components. The submission was after the deadline.

### Submission

- **Submission deadline: 2026.05.24**
- [**Submission form**]()

## Lecture

- I.    [Tokenization](../materials/NLP-A/lectures/lesson_2)
- I.    [Text representation I.](../materials/NLP-A/lectures/lesson_3)
- I.    [Text representation II.](../materials/NLP-A/lectures/lesson_4)
- II.   [Large language models I. fancy-rnn](https://robertlakatos.github.io/me/materials/NLP-A/lectures/fancy-rnn.pdf)
- II.   [Large language models I. CNN-TreeRNN](https://robertlakatos.github.io/me/materials/NLP-A/lectures/CNN-TreeRNN.pdf)
- III.  [Large language models II. Basic](https://robertlakatos.github.io/me/materials/NLP-A/lectures/rnnlm.pdf)
- III.  [Large language models II. Transformer](https://robertlakatos.github.io/me/materials/NLP-A/lectures/transformers.pdf)
- IV.   [Pretrain](https://robertlakatos.github.io/me/materials/NLP-A/lectures/pretraining-updated.pdf) - podcast : [hu](https://youtu.be/Dyus4v-qnGk) / [en](https://youtu.be/57PFlOeFKvM)
- IV.   [Question Answering](https://robertlakatos.github.io/me/materials/NLP-A/lectures/QA.pdf) - podcast [hu](https://youtu.be/P8W2NkV1fWk)
- V.    [Prompting RLHF](https://robertlakatos.github.io/me/materials/NLP-A/lectures/prompting-rlhf.pdf) - podcast [hu](https://youtu.be/xQTA4Tjvidc) / [en](https://youtu.be/3K_cRNOq5vI)
- VI.   [Life After DPO](https://robertlakatos.github.io/me/materials/NLP-A/lectures/life-after-dpo-lambert.pdf)
- VI.   [Training](https://robertlakatos.github.io/me/materials/NLP-A/lectures/training.pdf)
- VII. [Efficient Adaptation](https://robertlakatos.github.io/me/materials/NLP-A/lectures/adaptation.pdf)

## Labor

### Basics

- I.    [Tokenization](https://colab.research.google.com/drive/1Z9XA9Ik9ofb_hk61mukq-P1X9JEpv1m4#scrollTo=gtFbC4F-H0h7)
- II.   [Embedded vectors](https://colab.research.google.com/drive/1RRurVdRdYblE9ShU8kwzpmkToAW67iIG#scrollTo=tsfToJX1g3gW)
- III.  [Recurent Neural Network](https://colab.research.google.com/drive/1aMlFLC8rAZm68qincUte6fNQvawUBTY4)

### Transformers

- IV    [Transformers](https://colab.research.google.com/drive/13ypN4qvbdMUFREZKAF-U1f0d0aYn7U_Z) - (online)
- V.    [GPT](https://colab.research.google.com/drive/1IL5zR6215l0WmTi84GorO5d-N1XQOPm9) - (online)
- VI.   [BERT](https://colab.research.google.com/drive/1QdXMVKzw0xxmIG9BrhGbbjIK37bksIK0)

### Efficient

- VII.  [Parameter Efficient Fine Tuning (PEFT)](https://colab.research.google.com/drive/1nIAO0-DsfZqo9SDz_9sTr7uzqK57dWQp)

## Submitted

- [2025 Spring](../materials/NLP-A/submitted/2025-1)

## Usefull Links

- [Huggingface](https://huggingface.co/)
- [LlamaIndex](https://docs.llamaindex.ai/en/stable/)
- [Keras](https://keras.io/)
- [Tensorflow](https://www.tensorflow.org/)
- [Pytorch](https://pytorch.org/)
- [Pyton](https://www.python.org/)
- [Google Colab](https://colab.google/)

## Recommended Literatures and Courses

1.  [Jurafsky, Daniel, and James H. Martin. "Speech and language processing (draft)." Chapter A: Hidden Markov Models (Draft of September 11, 2018). Retrieved March 19 (2018): 2019.](https://ms.b-ok.xyz/book/3560643/4a6ab2)
2.  [Eisenstein, Jacob. "Introduction to natural language processing." MIT press, 2019.](https://mitpress.mit.edu/9780262042840/introduction-to-natural-language-processing/)
3.  [Goldberg, Yoav. "A primer on neural network models for natural language processing." Journal of Artificial Intelligence Research 57 (2016): 345-420.](https://arxiv.org/pdf/1510.00726.pdf)
4.  [Francois Chollet. "Deep Learning with Python"](https://www.amazon.com/Deep-Learning-Python-Francois-Chollet/dp/1617294438)
5.  [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/chapter0/1?fw=pt)
6.  [MIT Introduction to Deep Learning](http://introtodeeplearning.com/)
7.  [Visual Guide to Transformer Neural Networks - (Episode 1)](⁠https://www.youtube.com/watch?v=dichIcUZfOw)
8.  [Visual Guide to Transformer Neural Networks - (Episode 2)](⁠https://www.youtube.com/watch?v=mMa2PmYJlCo)
9.  [Visual Guide to Transformer Neural Networks - (Episode 3)](⁠https://www.youtube.com/watch?v=gJ9kaJsE78k)
10. [Stanford CS 224N / Ling 280  —  Natural Language Processing](https://web.stanford.edu/class/cs224n/)

# Usefull Publications

[1] [Attention Is All You Need](https://arxiv.org/pdf/1706.03762.pdf)

[2] [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)

[3] [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)

[4] [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)

[5] [Global Vectors for Node Representations](https://arxiv.org/pdf/1902.11004.pdf)