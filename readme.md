# custom whisper api

The objective of this repository is *make a basic a functional* speech to text api *configurable* and *escalable* . The api use a powerful speech to text model, [whisper](https://github.com/openai/whisper),

## Setup

1. Create a python environment/ enable the environment
    
    - Windows

``` bash
python -m venv .venv
.venv/Script/activate
```

  - Linux/Macos

```bash
python3 -m virtualenv .venv
source .venv/bin/activate
```

  - Conda (recommended)

```bash
conda create --name whisper python=3.10 --yes
conda activate whisper
```

2. Download dependencies


```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

```
pip install -r requirements.txt
```

3. Run

```
    uvicorn app:app --reload
```

4. Docker

```
    docker run -d --name WhisperAPI -p8000:80 danielsarmiento04/custom_whisper_api:1
```
