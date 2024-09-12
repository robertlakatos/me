---
title: "Text Cleaning"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-I/labor/II-text-cleaning-II
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-09-12
location: "Debrecen, Hungary"
---

[Colab link](https://colab.research.google.com/drive/10-elAxQ67cDiqjnGio_rXMhIkGKkPEGH)

## Huggingface

- IMDB dataset: hf://datasets/scikit-learn/imdb/IMDB Dataset.csv

## Whitespace kezelése (Handling Whitespaces)

Hungary: A felesleges szóközök, tabulátorok, sortörések eltávolítása vagy normalizálása, hogy a szöveg homogén legyen.

English: Removing or normalizing unnecessary spaces, tabs, line breaks, so that the text is homogeneous.

## Speciális karakterek eltávolítása (Removing Special Characters)

Hungary: Speciális karakterek, mint például @, #, %, eltávolítása, amelyek általában nem relevánsak a szöveg értelmezésében.

English: Removing Special Characters: Removing special characters such as @, #, %, which are generally not relevant to the interpretation of the text.

## HTML címkék eltávolítása (Removing HTML Tags)

Hungary: Webes szövegek esetén a HTML tag-ek eltávolítása, amelyek nem tartoznak a tényleges szöveghez.

English: In the case of web texts, removing HTML tags that do not belong to the actual text.

## Kontrakciók kibontása (Expanding Contractions)

Hungary: Az olyan rövidítések kibontása, mint a "don't" → "do not", hogy egyértelműbb legyen a szöveg jelentése.

English: Expanding abbreviations such as "don't" → "do not" to make the meaning of the text clearer.

## Ékezetek és diakritikus jelek eltávolítása (Removing Accents and Diacritics)

Hungary: Az ékezetes és diakritikus jelek eltávolítása vagy normalizálása, például „á” → „a”, hogy egységesebb legyen a szöveg.

English: Removing or normalizing accents and diacritics, such as "á" → "a", to make the text more consistent.

## Szólisták használata (Using Wordlists)

Hungary: Olyan speciális szólisták használata, amelyek alapján kiszűrhetőek bizonyos nem kívánt szavak vagy szószerkezetek.

English: Using special wordlists that filter out certain unwanted words or word structures.