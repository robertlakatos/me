---
title: "Text Cleaning"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-I/labor/I-text-cleaning
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

## Whitespace kezelése (Handling Whitespaces):

Hungary: A felesleges szóközök, tabulátorok, sortörések eltávolítása vagy normalizálása, hogy a szöveg homogén legyen.

English: Removing or normalizing unnecessary spaces, tabs, line breaks, so that the text is homogeneous.

## Speciális karakterek eltávolítása (Removing Special Characters):

Hungary: Speciális karakterek, mint például @, #, %, eltávolítása, amelyek általában nem relevánsak a szöveg értelmezésében.

English: Removing Special Characters: Removing special characters such as @, #, %, which are generally not relevant to the interpretation of the text.

## Tokenizáció (Tokenization):

Hungary: A szöveg szavakra vagy mondatokra való bontása (tokenek), amely az első lépés a szöveg strukturálásában.

English: Breaking the text into words or sentences (tokens), which is the first step in structuring the text.

## HTML címkék eltávolítása (Removing HTML Tags):

Hungary: Webes szövegek esetén a HTML tag-ek eltávolítása, amelyek nem tartoznak a tényleges szöveghez.

English: In the case of web texts, removing HTML tags that do not belong to the actual text.

## Kontrakciók kibontása (Expanding Contractions):

Hungary: Az olyan rövidítések kibontása, mint a "don't" → "do not", hogy egyértelműbb legyen a szöveg jelentése.

English: Expanding abbreviations such as "don't" → "do not" to make the meaning of the text clearer.

## Ékezetek és diakritikus jelek eltávolítása (Removing Accents and Diacritics):

Hungary: Az ékezetes és diakritikus jelek eltávolítása vagy normalizálása, például „á” → „a”, hogy egységesebb legyen a szöveg.

English: Removing or normalizing accents and diacritics, such as "á" → "a", to make the text more consistent.

## Szólisták használata (Using Wordlists):

Hungary: Olyan speciális szólisták használata, amelyek alapján kiszűrhetőek bizonyos nem kívánt szavak vagy szószerkezetek.

English: Using special wordlists that filter out certain unwanted words or word structures.