---
title: "Neural Network"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-I/labor/V-neural-network
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-10-03
location: "Debrecen, Hungary"
---

[Colab link](https://colab.research.google.com/drive/14U2JZ93kx78zzYxgviLZg3_qd9nSz5Qt)

This notebook demonstrates the process of performing **text classification** on text data, using the [AG News](https://huggingface.co/datasets/fancyzhx/ag_news) dataset as an example.

## Here's a breakdown of the key concepts covered:

- Text Cleaning:
    - Converting text to lowercase.
    - Removing extra whitespaces, special characters, HTML or XML tags, and punctuation.
    - Expanding contractions.
    - Removing numbers and stop words.
    - Lemmatizing words.

- Data Splitting (training, validation and test): Dividing the dataset into training, validation, and test sets for model training and evaluation.

- Vectorization (Feature Extraction):
        Using CountVectorizer to convert text into numerical representations based on word counts.
        Using TF-IDF vectorizer to weigh word importance based on frequency.

- Model Building:
        Creating a simple neural network with a softmax activation function for classification.
        Compiling the model using an appropriate optimizer, loss function, and metrics.

- Model Training and Evaluation: Training the model on the training data and evaluating its performance on the test data using metrics like accuracy.