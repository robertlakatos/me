---
title: "Introduction to AI and Decision Making"
collection: teaching
type: "B.Sc course"
permalink: materials/AIPD/labor/IX-decision-trees
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 205-11-19
location: "Debrecen, Hungary"
---

# Deecision trees

[Colab link](https://colab.research.google.com/drive/1SH8A4R6D6fAXsQB5pGUr8s7XvkUDvHUr)

## Theoretical background

In Machine Learning, a Decision Tree is a supervised learning algorithm used for both classification (predicting a category) and regression (predicting a number).

Think of it as a digital version of the game "20 Questions." It arrives at a conclusion by asking a series of Yes/No questions, narrowing down the possibilities until it reaches a specific answer.

### 1. The Anatomy of a Decision Tree

A decision tree looks like an upside-down tree. It starts at the top and branches downward.

- **Root Node:** The very top of the tree. This represents the entire dataset before any decisions are made. It asks the first, most important question to split the data.
- **Decision Nodes (Internal Nodes):** These are the points in the middle of the tree where the data is split further based on specific features (e.g., "Is the weather sunny?").
- **Branches:** The arrows connecting nodes, representing the outcome of a decision (e.g., "Yes" or "No").
- **Leaf Nodes (Terminal Nodes):** The bottom-most nodes that do not split any further. These represent the final output or prediction (e.g., "Play Tennis" or "Don't Play").

### 2. How It Works

The goal of the algorithm is to split the data into groups that are as "pure" as possible. A "pure" group contains data points that mostly belong to the same class.
- **Splitting:** The algorithm looks at all possible features in your data and decides which one splits the data best.
- **Measuring Purity:** It uses mathematical metrics to evaluate the split. The most common are:
- **Gini Impurity:** Measures how often a randomly chosen element would be incorrectly labeled.
- **Entropy:** Measures the disorder or uncertainty in the data.

The algorithm calculates the Information Gain (IG) to choose the split that reduces disorder the most.

Recursion: It repeats this process for every branch until the leaf nodes are pure enough or the tree reaches a maximum depth.

## 3. A Simple Example

Imagine you are building a model to decide if you should wear a jacket.

1. **Root Node:** Is it raining?
    - If **Yes:** Wear Jacket (Leaf Node).
    - If **No:** Go to next decision node.
2. **Decision Node:** Is the temperature below 20°C?
    - If **Yes:** Wear Jacket (Leaf Node).
    - If **No:** Don't Wear Jacket (Leaf Node).

## 4. Advantages & Disadvantages

Advantages	
- **Interpretable:** Humans can easily understand the logic by looking at the drawing.	
- **No Scaling Needed:** You don't need to normalize or scale your data (unlike Neural Networks).	
- **Versatile:** Handles both numerical (Age: 25) and categorical (Color: Red) data.	

Disadvantages
- **Overfitting:** Trees can become too complex and memorize noise in the data (learning the specific examples rather than the rules).
- **Instability:** A small change in the data can lead to a completely different tree structure.
- **Greedy:** It makes the best optimal choice at the current step, which might not lead to the best overall global tree.