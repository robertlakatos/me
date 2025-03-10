---
title: "Filter and Cluster"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/labor/filter-cluster
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2025-03-03
location: "Debrecen, Hungary"
---

## [Colab](https://colab.research.google.com/drive/1TfXeT5C4yzA7UaHx8PdVeVxPamwC-xWx)

The labor aims to filter, cluster and visualize the CORD-19 dataset metadata. It uses various libraries and techniques for this purpose.

## Summary

- **Data Download:** The notebook starts by downloading the CORD-19 dataset metadata using the kagglehub library.
- **Data Filtering:** The metadata is then filtered to keep only the entries with a non-null description using pandas DataFrame operations.
- **Keyword Extraction:** The KeyBERT library is planned to be used to extract relevant keywords from the descriptions of the filtered metadata.
- **Clustering:** The BERTTopic library is intended to be applied to cluster the metadata based on the extracted keywords and semantic similarity.
- **Dimension Reduction:** The Umap library is planned for reducing the dimensionality of the clustered data for visualization purposes.
- **Visualization:** Finally, the results of the clustering and dimension reduction are visualized.

## Theoretical Background

- **CORD-19 Dataset:** The CORD-19 dataset is a collection of research articles related to COVID-19. The metadata contains information about each article, such as title, authors, abstract, and publication date.
- **Keyword Extraction:** KeyBERT is a keyword extraction technique that uses BERT embeddings to identify the most relevant words or phrases in a document. It can be used to extract the main topics or themes of a text.
- **Topic modelling:** BERTTopic is a topic modeling technique that leverages BERT embeddings and clustering algorithms to group similar documents together. It can be used to discover hidden topics in a collection of texts.
- **Dimension Reduction:** Umap (Uniform Manifold Approximation and Projection) is a dimensionality reduction technique that can be used to visualize high-dimensional data in a lower-dimensional space. It preserves the local structure of the data while reducing its complexity.
- **HDBSCAN clustering:** HDBSCAN - Hierarchical Density-Based Spatial Clustering of Applications with Noise. Performs DBSCAN over varying epsilon values and integrates the result to find a clustering that gives the best stability over epsilon. This allows HDBSCAN to find clusters of varying densities (unlike DBSCAN), and be more robust to parameter selection.
- **Visualization:** The visualization step aims to represent the clustered data in a human-readable format, such as a scatter plot or a network diagram. This allows users to explore the relationships between different documents and topics.

## Libraries Used

- **kagglehub:** For downloading the CORD-19 dataset.
- **pandas:** For data manipulation and analysis.
- **KeyBERT:** For keyword extraction.
- **BERTTopic:** For clustering.
- **Umap:** For dimension reduction.
