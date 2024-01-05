# **Whisper API**

## Resume
The objective of this repository is *make a basic a functional* speech to text api *configurable* and *escalable* . The api use a powerful speech to text model, [whisper](https://github.com/openai/whisper),

## Table Of Contents
- [Set UP](#setup)
- [Next Steps](#next-steps)
- [License](#license)
- [References](#references)

## Setup


1. Download dependencies


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

2. Create a python environment / enable the environment

    ```
    conda create --name whisper python=3.10 -y
    conda activate whisper
    pip install -r requirements.txt
    ```


3. Run

    ```
    uvicorn app:app --reload
    ```
-  Docker

    ```
    docker run -d --name WhisperAPI -p8000:80 danielsarmiento04/custom_whisper_api:1
    ```

## Next Steps

1. Websocket service, idea

## License

This repository is licensed under the [Apache 2.0](LICENSE) License.


## References

[1] Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2022). Robust Speech Recognition via Large-Scale Weak Supervision. doi:10.48550/ARXIV.2212.04356

[2] Ramírez, S. FastAPI [Computer software]. https://github.com/tiangolo/fastapi

[3]