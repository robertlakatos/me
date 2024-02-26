---
title: "Generative AI - Chat model"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/gaichat
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024
location: "Debrecen, Hungary"
---

## [LLaMA model](https://ai.meta.com/llama/)

```python
!pip install transformers torch accelerate
```

```python
from huggingface_hub import notebook_login

notebook_login()
```

```python
model = "meta-llama/Llama-2-7b-hf"
```

```python
import torch
from transformers import AutoTokenizer
from transformers import GenerationConfig
from transformers import AutoModelForCausalLM
```

```python
tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForCausalLM.from_pretrained(model,
                                             torch_dtype=torch.bfloat16,
                                             device_map="auto")
```

```python
!nvidia-smi
```

```python
prompt = "Do you know what the best move is by imdb?"
```

```python
inputs = tokenizer(
    prompt,
    return_tensors="pt",
)
input_ids = inputs["input_ids"].cuda()

input_ids
```

```python
generation_config = GenerationConfig(
    temperature=0.6,
    top_p=0.95,
    do_sample=True,
    repetition_penalty=1.2,
)
```

```python
# print("Generating...")
generation_output = model.generate(
    input_ids=input_ids,
    generation_config=generation_config,
    return_dict_in_generate=True,
    output_scores=True,
    min_new_tokens=0,
    max_new_tokens=256,
    pad_token_id = 0,
    eos_token_id = 50256
)
```

```python
for s in generation_output.sequences:
  print(tokenizer.decode(s))
```