from whisper.tokenizer import (
    LANGUAGES,
    TO_LANGUAGE_CODE
)

import logging

ALLOW_EXTENSIONS = {
    'wav',
    'mp3',
    'mov',
    'mpeg',
    'x-wav'
}

ALLOW_CODEC = 'pcm_s16le'

