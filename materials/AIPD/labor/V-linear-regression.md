---
title: "Introduction to AI and Decision Making"
collection: teaching
type: "B.Sc course"
permalink: materials/AIPD/labor/V-linear-regression
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-10-07
location: "Debrecen, Hungary"
---

[Colab link](https://colab.research.google.com/drive/1sIXiLMUMcxdY4gyF4Ex2p3RKx1qy43eR)

[Colab link solved](https://colab.research.google.com/drive/1EaR0ro3CO6Ccq2Noi06xeLpGdCjH7cro?authuser=2)

This notebook demonstrates the process of performing sentiment analysis on text data, using the IMDB dataset as an example.

## Here's a breakdown of the key concepts covered:

- Text Cleaning:
    - Converting text to lowercase.
    - Removing extra whitespaces, special characters, HTML tags, and punctuation.
    - Expanding contractions.
    - Removing numbers and stop words.
    - Lemmatizing words.

- Data Splitting (training, validation and test): Dividing the dataset into training, validation, and test sets for model training and evaluation.

- Vectorization (Feature Extraction):
        Using CountVectorizer to convert text into numerical representations based on word counts.
        Using TF-IDF vectorizer to weigh word importance based on frequency.

- Model Building:
        Creating a simple logistic regression with a sigmoid activation function for binary classification (positive or negative sentiment).
        Compiling the model using an appropriate optimizer, loss function, and metrics.

- Model Training and Evaluation: Training the model on the training data and evaluating its performance on the test data using metrics like accuracy.