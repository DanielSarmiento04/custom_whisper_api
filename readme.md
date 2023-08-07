# custom whisper api

The objective of this repository is *make a basic a functional* speech to text api *configurable* and *escalable* . The api use a powerful speech to text model, [whisper](https://github.com/openai/whisper),

## Setup

1. Create a python environment
    
    - Windows

``` 
    python -m venv .venv
```

  - Linux/Macos

```
    python3 -m virtualenv .venv
```

  - Conda (recommended)

```
    conda create --name whisper python=3.10 --yes
```


## load

uvicorn app:app --reload