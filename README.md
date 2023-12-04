# llm-notebooks

Few notebooks to play with LLM's like Openjourney, Stable Diffusion, etc.

You need to be authenticated in Hugging Face in order to use it.

## Installation

```bash
git clone https://github.com/mikelogaciuk/llm-notebooks.git
cd llm-notebooks
virtualenv venv && source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Just edit the prompt and run it.

## Scaling models
Models copied from other repositories on GitHub.

All rights to them are reserved to their respective owners.

## Samples

### SDXL-Turbo

![#1](./samples/B6h9r3Q0Q11L6g3p1m6a4g7T9.png)

![#2](./samples/M0U8R5l5F12f10d0w8U8M8V8N1.png)

![#3](./samples/O9k1f11B12R3m12Y7m8i3n5K2u9.png)

## Note

Please note that only **SDXL-Turbo** can generate images in reasonable time on CPU (about 4 seconds on 10C/16T CPU).

The rest of the models demand nVidia GPU (at least 4070) in order to speed up.