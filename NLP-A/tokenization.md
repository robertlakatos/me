---
title: "Tokenization"
collection: teaching
type: "M.Sc course"
permalink: /NLP-A/tokenization
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024
location: "Debrecen, Hungary"
---

# Tokenizáció

- A mondatok szavakra, szórészekre vagy karakterekre történő darabolása
- Fajtái:
    - Karakter alapú
    - Szó, alszó alapú
- Cél: A feldolgozni kívánt adathalmaz szavakra vagy karakterekre történő tördelése olyan módon hogy az analízishez felhasznált gépi tanuló eljárás a saját szótára segítségével azt beazonosítani tudja.
- Trade-off: méret vs hatékonyság

```python
!pip install transformers
```

## Karakter alapú tokenizáció

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

## WordLevel alapú tokenizáció

Ez a „klasszikus” tokenizációs algoritmus. Egyszerűen leképezheti a szavakat az azonosítókra anélkül, hogy bármi különösebb lenne. Ennek az az előnye, hogy nagyon egyszerűen használható és érthető, de a jó lefedettséghez rendkívül nagy szókincsre van szükség. Ez a modell nem fog közvetlenül választani, egyszerűen leképezi a bemeneti tokeneket az azonosítókra.

### NLTK

```python
import nltk
nltk.download('punkt')
```

```python
from nltk.tokenize import word_tokenize

s = '''Good muffins cost $3.88\nin New York.  Please buy me two of them.\n\nThanks.'''
word_tokenize(s)
```

### Hugging Face

```python
from tokenizers.pre_tokenizers import Whitespace

pre_tokenizer = Whitespace()
pre_tokenizer.pre_tokenize_str("Hello! How are you? I'm fine, thank you.")
```

## BPE

Az egyik legnépszerűbb alszó tokenizációs algoritmus. A Byte-Pair-Encoding úgy működik, hogy karakterekkel kezdődik, miközben a leggyakrabban láthatókat egyesíti, így új tokeneket hoz létre. Ezután iteratívan dolgozik, hogy új tokeneket építsen a korpuszban látható leggyakoribb párokból. A BPE olyan szavakat tud felépíteni, amelyeket soha nem látott több részszó token használatával, ezért kisebb szókincsre van szüksége, és kisebb az esélye annak, hogy „unk” (ismeretlen) tokenjei vannak.

```python
import io
import requests
import zipfile

url = "https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-raw-v1.zip"
r = requests.get(url, stream =True)
check = zipfile.is_zipfile(io.BytesIO(r.content))

while not check:
    r = requests.get(url, stream =True)
    check = zipfile.is_zipfile(io.BytesIO(r.content))
else:
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
```

### Speciális tokenek
- [UNK] ismeretlen token jelölése
- [CLS] teljes mondatot reprezentáló token
- [SEP] mondat szeparátor token
- [PAD] padding token a fix input hossz feltöltését biztosító token
- [MASK] Maszkolást biztosító token. pl.: "Hello I'm a [MASK] model."

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
files = [f"wikitext-103-raw/wiki.{split}.raw" for split in ["test", "train", "valid"]]

tokenizer.train(files, trainer)
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

## Encoding in a batch

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

## Pretrained tokenizer, használata

- BERT
- WordPiece: Ez a BPE-hez nagyon hasonló részszó-tokenizációs algoritmus, amelyet főként a Google használ olyan modellekben, mint a BERT. Mohó algoritmust használ, amely először hosszú szavakat próbál felépíteni. Ez eltér a BPE-től, amely karakterekből indul ki, és minél nagyobb tokeneket épít. A híres ## előtagot használja a szó részét képező jelzők azonosítására (azaz nem kezdődő szó).

```python
import requests

url = "https://huggingface.co/nlpaueb/legal-bert-base-uncased/raw/main/vocab.txt"
response = requests.get(url)

with open("bert-vocab.txt", "w") as f:
  f.write(response.text)
```

```python
from tokenizers import BertWordPieceTokenizer

tokenizer = BertWordPieceTokenizer("bert-vocab.txt", lowercase=True)
```

```python
output = tokenizer.encode("Hello, y'all!", "How are you 😁 ?")
print(output.tokens)
```

### Saját WordPiece építése
Ugyanúgy mint a BPE-nél csak használjuk a WordPiece libet

```python
from tokenizers.models import WordPiece
```

## Unigram
Az Unigram egy részszó tokenizációs algoritmus is, és úgy működik, hogy megpróbálja azonosítani a legjobb részszó tokenek készletet, hogy maximalizálja az adott mondat valószínűségét. Ez abban különbözik a BPE-től, hogy nem determinisztikus, szekvenciálisan alkalmazott szabályok alapján. Ehelyett az Unigram képes lesz többféle tokenizálási módot kiszámítani, miközben kiválasztja a legvalószínűbbet.

```python
from tokenizers.models import Unigram
```