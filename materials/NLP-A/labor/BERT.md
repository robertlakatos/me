---
title: "BERT"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/BERT
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-03-21
location: "Debrecen, Hungary"
---

This Colab notebook demonstrates the process of fine-tuning a DistilBERT model for sentiment classification on the Stanford IMDB dataset. Here's a breakdown of the steps involved:

1. **Installation:** Installs necessary libraries like transformers, datasets, evaluate, accelerate, peft, and bitsandbytes.
2. **Dataset Loading:** Loads the IMDB dataset using the datasets library.
3. **Data Preparation:** Tokenizes the dataset using the AutoTokenizer from the transformers library and prepares it for training using DataCollatorWithPadding.
4. **Evaluation Metric:** Loads the accuracy metric using evaluate.
5. **Model Loading:** Loads a pre-trained DistilBERT model using AutoModelForSequenceClassification.
6. **Training:** Fine-tunes the model using the Trainer from the transformers library.
7. **LoRA (Low-Rank Adaptation):** Applies LoRA (Low-Rank Adaptation) to the model for efficient fine-tuning.
8. **Training with LoRA:** Fine-tunes the model again, this time with LoRA applied, to improve performance.

In essence, the notebook showcases a standard workflow for sentiment classification using the Hugging Face Transformers library and incorporates LoRA for enhanced fine-tuning.

## [Colab](https://colab.research.google.com/drive/1QdXMVKzw0xxmIG9BrhGbbjIK37bksIK0)