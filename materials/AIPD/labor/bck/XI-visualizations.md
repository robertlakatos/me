---
title: "Introduction to AI and Decision Making"
collection: teaching
type: "B.Sc course"
permalink: materials/AIPD/labor/XI-visualizations
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-12-03
location: "Debrecen, Hungary"
---

# Visualizations

[Colab link](https://colab.research.google.com/drive/1tHD2cGYFGH7C7kntbGMMVANU08tS8Zii)

Data visualization plays a key role in understanding data and evaluating artificial intelligence (AI) models, especially with large data sets where raw data can be difficult to review. Here are some key areas where visualization can help:

1. Understanding and preparation of data:
- Discovering Patterns and Trends: Graphs and figures make it easier to spot patterns, trends, and anomalies in your data. These can be crucial when preparing the model, for example in identifying predictive variables.
- Missing data: Visualizing missing data, such as using a heatmap or boxplot, shows where there are problems in the data set, which is important during cleaning.

2. Model performance evaluation:
- Confusion matrix: One of the most common tools used to evaluate classification models. It helps to understand which classes the model gets wrong or which classes it predicts correctly.
- Receiver Operating Characteristic (ROC) and Precision-Recall curves: These curves help analyze the performance of classification models, especially when the balance between classes is disturbed.
- Learning curves: They depict the change of the model's training and validation errors over time, helping to recognize the model's overfitting or underfitting problems.

3. Detection of anomalies:
- Time series analyses: Visualizing time-based data can help identify anomalies and outliers. An example of this is the unexpected price fluctuations that arise when predicting oil prices.
- PCA (principal component analysis), umpa and t-SNE: With the help of such techniques, it is possible to visualize large-dimensional data sets, where the clustering or dispersion of the data can clearly show anomalies.

4. Decision-making support:
- Interpretability techniques: Modell weights and parameters can be used to visually represent how a model makes its decisions, which helps decision makers understand what factors play into the predictions.