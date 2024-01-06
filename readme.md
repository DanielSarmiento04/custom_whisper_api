# **Whisper API**

## Abstract

Whisper API is a *functional ans scalable* speech to text API developed using Python and [whisper](https://github.com/openai/whisper) as base. The objective of this repository is give some easy to configure base api to integrate in some special case, for this purpose is necessary to take that we use a client-side pattern (it's possible to change depending of the case). Also, we give the docker container to simplify the test and the deployment, check de package zone.


## Table Of Contents
- [Set UP](#setup)
- [Next Steps](#next-steps)
- [License](#license)
- [References](#references)

## Setup


1. Download dependencies


    ```bash
    # on Ubuntu or Debian
    sudo apt update && sudo apt install ffmpeg  libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev

    # on Arch Linux
    sudo pacman -S ffmpeg libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev 

    # on MacOS using Homebrew (https://brew.sh/)
    brew install ffmpeg pyaudio

    # on Windows using Chocolatey (https://chocolatey.org/)
    choco install ffmpeg pyaudio

    # on Windows using Scoop (https://scoop.sh/)
    scoop install ffmpeg pyaudio
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
    docker run -d --name WhisperAPI -p8000:80 ghcr.io/danielsarmiento04/custom_whisper_api:latest
    ```

## Next Steps

1. Websocket service, idea

## License

This repository is licensed under the [Apache 2.0](LICENSE) License.


## References

[1] Radford, A., Kim, J. W., Xu, T., Brockman, G., McLeavey, C., & Sutskever, I. (2022). Robust Speech Recognition via Large-Scale Weak Supervision. doi:10.48550/ARXIV.2212.04356

[2] Ramírez, S. FastAPI [Computer software]. https://github.com/tiangolo/fastapi
