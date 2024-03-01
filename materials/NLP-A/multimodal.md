---
title: "Multimodal use cases"
collection: teaching
type: "M.Sc course"
permalink: /materials/NLP-A/multimodal
venue: "University of Debrecen, Department of Data Science and Visualization"
date: 2024-02-27
location: "Debrecen, Hungary"
---

```python
!pip install diffusers
!pip install accelerate
!pip install --upgrade pip
!pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate datasets[audio]

# Restart env!
```

## [CLIP](https://huggingface.co/docs/transformers/model_doc/clip)

<img src="https://images.openai.com/blob/fbc4f633-9ad4-4dc2-bd94-0b6f1feee22f/overview-a.svg?width=10&height=10&quality=50" alt="clip">

Figure 1: Contrastive pre-training: [openai.com](https://openai.com/research/clip).


<img src="https://images.openai.com/blob/d9d46e4b-6d6a-4f9e-9345-5c6538b1b8c3/overview-b.svg?width=10&height=10&quality=50" alt="clip">

Figure 2: Create dataset classifier from label text: [openai.com](https://openai.com/research/clip).

```python
import requests

from PIL import Image
from transformers import CLIPModel
from transformers import CLIPProcessor
```

```python
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
```

```python
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
```

```python
inputs = processor(text=["a photo of a cat", "a photo of a dog"],
                   images=image,
                   return_tensors="pt",
                   padding=True)
```

```python
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1)
probs
```

## Text To Image - Stable Diffusion

- https://huggingface.co/docs/diffusers/training/text2image
- https://huggingface.co/tasks/text-to-image

```python
from diffusers import EulerDiscreteScheduler
from diffusers import StableDiffusionPipeline
```

```python
import torch

model_id = "stabilityai/stable-diffusion-2"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
```

```python
prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]
image
```

## [Wishper](https://huggingface.co/openai/whisper-large-v3)

[paper](https://arxiv.org/pdf/2212.04356.pdf)

<img src="https://miro.medium.com/v2/resize:fit:1200/1*DTln7B9C_42NUboKmuDkGQ.png" alt="wishper">
!sss
Figure 3!: Create dataset classifier from label text: [medium.com](https://kargarisaac.medium.com/whisper-robust-speech-recognition-via-large-scale-weak-supervision-4081fa089ff7).

```python
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset
```

```python
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
```

```python
model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)
```

```python
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)
```

```python
# https://huggingface.co/datasets/hf-internal-testing/librispeech_asr_dummy
dataset = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
dataset
```

```python
sample = dataset[0]["audio"]
result = pipe(sample)
print(result["text"])
```