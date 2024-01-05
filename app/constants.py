from whisper.tokenizer import (
    LANGUAGES,
    TO_LANGUAGE_CODE
)

import logging

from enum import Enum
from pydantic import BaseModel

ALLOW_EXTENSIONS = {
    'wav',
    'mp3',
    'mov',
    'mpeg',
    'x-wav'
}

ALLOW_CODEC = 'pcm_s16le'

class Extension(str, Enum):
    wav = "wav"
    mp3 = "mp3"
    mov = "mov"
    mpeg = "mpeg"
    x_wav = "x-wav"


class AudioWS(BaseModel):
    extension: Extension
    sample_rate: int
