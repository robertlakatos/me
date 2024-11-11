---
title: "Tokenization"
collection: teaching
type: "B.Sc course"
permalink: /materials/NLP-I/labor/II-tokenization
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-09-05
location: "Debrecen, Hungary"
---

[Colab link](https://colab.research.google.com/drive/1eGKpNV4mVnX35beXJRQuX1G5nbm9Un9q)

```python
!pip install transformers
!pip install datasets
```

# Tokenizáció (Tokenization)

- Magyar:
    - A mondatok szavakra, szórészekre vagy karakterekre történő darabolása
    - Fajtái:
        - Karakter alapú
        - Szó, alszó alapú
    - Cél: A feldolgozni kívánt adathalmaz szavakra vagy karakterekre történő tördelése olyan módon hogy az analízishez felhasznált gépi tanuló eljárás a saját szótára segítségével azt beazonosítani tudja.
    - Trade-off: méret vs hatékonyság

- English:
    - Splitting sentences into words, parts of words or characters
    - Varieties:
        - Character based
        - Word, subword based
    - Purpose: Breaking down the data set to be processed into words or characters in such a way that the machine learning process used for the analysis can identify it with the help of its own dictionary.
    - Trade-off: size vs efficiency

## Karakter alapú tokenizáció (Character-based tokenization)

```python
sentence = "I would like to work than machine lerning engineer at Google!".lower()
print(sentence)
```

```python
sentence = sentence.replace(" ","")
print(sentence)
```

```python
chars = [char for char in sentence]
print(chars)
```

```python
chars = list(set(chars))
print(chars)
```

```python
word_to_idx = {chars[i] : i for i in range(len(chars))}
word_to_idx
```

## WordLevel alapú tokenizáció (WordLevel based tokenization)

Magyar: Ez a „klasszikus” tokenizációs algoritmus. Egyszerűen leképezheti a szavakat az azonosítókra anélkül. Ennek az az előnye, hogy nagyon egyszerűen használható és érthető, de a jó lefedettséghez rendkívül nagy szókincsre van szükség. Ez a modell nem fog tanulni, egyszerűen leképezi a bemeneti szavakat az azonosítókra valamilyen szeparáló karakter például szóköz mentén.

Engilsh: This is the "classic" tokenization algorithm. You can map the words to the IDs without it. This has the advantage of being very simple to use and understand but requires an extensive vocabulary for good coverage. This model will not learn, it will simply map input words to identifiers along some separator character such as a space.

### With NLTK package

```python
import nltk

nltk.download('punkt')
```

```python
from nltk.tokenize import word_tokenize

s = '''Good muffins cost $3.88\nin New York.  Please buy me two of them.\n\nThanks.'''
word_tokenize(s)
```

### With Hugging Face package

```python
from tokenizers.pre_tokenizers import Whitespace

pre_tokenizer = Whitespace()
pre_tokenizer.pre_tokenize_str("Hello! How are you? I'm fine, thank you.")
```

## N-Gram

```python
# To Do with prompting
```

## [BPE](https://www.youtube.com/embed/HEikzVL-lZU)

<iframe width="1280" height="720" src="https://www.youtube.com/embed/HEikzVL-lZU" title="Byte Pair Encoding Tokenization" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Magyar: Az egyik legnépszerűbb alszó tokenizációs algoritmus. A Byte-Pair-Encoding úgy működik, hogy karakterekkel kezdődik, miközben a leggyakrabban láthatókat egyesíti, így új tokeneket hoz létre. Ezután iteratívan dolgozik, hogy új tokeneket építsen a korpuszban látható leggyakoribb párokból. A BPE olyan szavakat tud felépíteni, amelyeket soha nem látott több részszó token használatával, ezért kisebb szókincsre van szüksége, és kisebb az esélye annak, hogy „unk” (ismeretlen) tokenjei vannak.

English: One of the most popular keyword tokenization algorithms. Byte-Pair-Encoding works by starting with characters while combining the most frequently seen ones to create new tokens. It then works iteratively to build new tokens from the most frequent pairs seen in the corpus. BPE can build words you've never seen before using multiple subword tokens, so it needs a smaller vocabulary and is less likely to have "unk" (unknown) tokens.

```python
from datasets import load_dataset

dataset = load_dataset("wikitext", "wikitext-103-raw-v1")
dataset
```

```python
corpus = dataset["train"]["text"] + dataset["test"]["text"] + dataset["validation"]["text"]
len(corpus)
```

### Speciális tokenek (Special tokens)

- Magyar:
    - [UNK] ismeretlen token jelölése
    - [CLS] teljes mondatot reprezentáló token
    - [SEP] mondat szeparátor token
    - [PAD] padding token a fix input hossz feltöltését biztosító token
    - [MASK] Maszkolást biztosító token. pl.: "Hello I'm a [MASK] model."

- English:
    - Marking [UNK] unknown token
    - [CLS] token representing a complete sentence
    - [SEP] sentence separator token
    - [PAD] padding token is a token ensuring the filling of the fixed input length
    - [MASK] Masking token. eg: "Hello I'm a [MASK] model."

```python
from tokenizers import Tokenizer
from tokenizers.models import BPE

tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
print(tokenizer)
```

```python
from tokenizers.trainers import BpeTrainer

trainer = BpeTrainer(special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
print(trainer)
```

```python
from tokenizers.pre_tokenizers import Whitespace

tokenizer.pre_tokenizer = Whitespace()
```

```python
tokenizer.train_from_iterator(corpus, trainer)
```

```python
tokenizer.save("tokenizer-bpe-wiki.json")
```

```python
tokenizer = Tokenizer.from_file("tokenizer-bpe-wiki.json")
```

```python
output = tokenizer.encode("Hello, y'all! How are you 😁 ?")
print(output)
```

```python
print(output.tokens)
print(output.ids)
print(output.offsets[9])
```

```python
tokenizer.token_to_id("[SEP]")
```

```python
from tokenizers.processors import TemplateProcessing

tokenizer.post_processor = TemplateProcessing(
    single="[CLS] $A [SEP]",
    pair="[CLS] $A [SEP] $B:1 [SEP]:1",
    special_tokens=[
        ("[CLS]", tokenizer.token_to_id("[CLS]")),
        ("[SEP]", tokenizer.token_to_id("[SEP]")),
    ],
)
```

```python
print(output.tokens)
output = tokenizer.encode("Hello, y'all!", "How are you 😁 ?")
print(output.tokens)
```

```python
print(output.type_ids)
```

## Kötegelt feldolgozás (Encoding in a batch)

```python
tokenizer.enable_padding(pad_id=3, pad_token="[PAD]")
```

```python
output = tokenizer.encode_batch(["Hello, y'all!", "How are you 😁 ?"])
print(output[0].tokens)
print(output[1].tokens)
```

```python
print(output[0].attention_mask)
print(output[1].attention_mask)
```