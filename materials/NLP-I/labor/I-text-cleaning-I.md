---
title: "Text Cleaning"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-I/labor/I-text-cleaning-I
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-09-05
location: "Debrecen, Hungary"
---

[Colab link](https://colab.research.google.com/drive/1QhghhzwDliCOMkRygSLfv5fLKT4Mjro1#scrollTo=edOFZuXqbKwx)

## Huggingface

- IMDB dataset: hf://datasets/scikit-learn/imdb/IMDB Dataset.csv

## Kisbetűsítés (Lowercasing)

Hungary: Az összes karakter kisbetűvé alakítása, hogy elkerüljük az olyan problémákat, mint a nagybetűk és kisbetűk közötti különbségek (pl. "Apple" és "apple").

English: Converting all characters to lowercase to avoid problems such as differences between uppercase and lowercase letters (eg "Apple" and "apple").

## Írásjelek eltávolítása (Removing Punctuation)

Hungary: Az írásjelek (pl. pontok, vesszők, kérdőjelek) eltávolítása, mivel ezek gyakran nem relevánsak a szövegelemzés szempontjából.

English: Removing punctuation (e.g. periods, commas, question marks) as they are often not relevant for text analysis.

## Számok eltávolítása (Removing Numbers)

Hungary: A számok eltávolítása, mivel sok esetben nem hordoznak jelentős információt, bár bizonyos esetekben (pl. pénzügyi elemzések) fontosak lehetnek.

English: Removing numbers, as in many cases they do not carry significant information, although in some cases (e.g. financial analyses) they may be important.

## Stopword-ek eltávolítása (Removing Stopwords):

Hungary: A gyakran előforduló, de kevés információt hordozó szavak (pl. "a", "és", "de") eltávolítása.

English: Removing words that occur frequently but carry little information (e.g. "a", "and", "but").

## Szógyökér képzés (Stemming):

Hungary: A szavak szógyökére való egyszerűsítése, például a „futás”, „futott” és „futni” mind a „fut” szógyökérre alakítása.

English: Simplifying words to their stem, for example, turning "run", "ran" and "to run" into the root "run".

## Lemmatizálás (Lemmatization):

Hungary: A szavak alapalakra (lemmára) alakítása, amely figyelembe veszi a szavak szófaját is, például a „futott” szót „fut” alakra, a „gyorsabban” szót „gyors” alakra hozza vissza.

English: Transforming words into basic forms (lemmas), which also takes into account the part of speech of the words, for example, returning the word "ran" to the form "run" and the word "faster" to the form "quick".