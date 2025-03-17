---
title: "Embedding"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/recurent-neural-network
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-03-17
location: "Debrecen, Hungary"
---

## [Colab](https://colab.research.google.com/drive/1RRurVdRdYblE9ShU8kwzpmkToAW67iIG)

## What is a Word Embedding?

A word embedding is a learned representation for text where words that have the same meaning have a similar representation. It is a dense vector representation of a word, unlike a sparse (and large) one-hot encoded vector. Word2Vec is a popular technique used to learn word embeddings.

## Why are Word Embeddings Important?

- **Capture Semantic Relationships:** They capture semantic relationships between words, allowing machine learning models to understand that words like "king" and "queen" are related in a way that "king" and "table" are not.
- **Improve Model Performance:** Using word embeddings as input features can significantly improve the performance of machine learning models on various natural language processing (NLP) tasks such as text classification, sentiment analysis, and machine translation.
- **Reduce Dimensionality:** They can reduce the dimensionality of text data, making it easier to process and analyze.
- **Transfer Learning:** Pre-trained word embeddings can be used to transfer knowledge to new NLP tasks, reducing the need for large amounts of labeled training data.

In summary, word embeddings like those learned by Word2Vec are an important tool for representing text in a way that captures semantic meaning and improves the performance of machine learning models. They are widely used in various NLP tasks.

This notebook demonstrates how to create word embeddings using the Word2Vec algorithm, specifically the Continuous Bag-of-Words (CBOW) model. It utilizes the IMDb dataset from Hugging Face Datasets for training.

### Data Loading and Preprocessing:
- The notebook begins by loading the IMDb dataset (train and test splits) from Hugging Face Datasets.
- It then preprocesses the text data by tokenizing it, removing stop words, and applying stemming using NLTK.
- A vocabulary is created based on the frequency of words in the dataset, with the most frequent words assigned unique indices.

### Creating Training Data:
- Context-target pairs are generated from the text data using a sliding window approach. Each pair consists of a target word and its surrounding context words.
- These pairs are used to train the Word2Vec model.

### Model Creation and Training:
- A CBOW Word2Vec model is implemented using PyTorch.
- The model is trained using the context-target pairs, optimizing to predict the target word given its context.
- The training process involves feeding batches of data to the model, calculating the loss, and updating the model's parameters to minimize the loss.

### Saving the Embeddings:
- After training, the word embeddings (vector representations of words) are extracted from the model.
- These embeddings are saved to two files: "vectors.tsv" containing the embedding vectors and "metadata.tsv" containing the corresponding words.

In essence, this notebook showcases the process of building a Word2Vec model to learn word embeddings from a large text dataset, which can be further used for various natural language processing tasks. I hope this helps! Let me know if you have any other questions.