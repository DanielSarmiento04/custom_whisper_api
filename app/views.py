from . import app
import whisper
import ffmpeg
import torch
from fastapi import (
    UploadFile
)
from .utils import(
    get_audio_properties,
    convert_audio_compatibility
)
import numpy as np

@app.get("/")
async def root():
    '''
        Base endpoint to test if the server is running
    '''
    return {"message": "Hello World"}

model = whisper.load_model(
    name="base"
)


@app.post('/transcribe')
def transcribe(audio:UploadFile):
    '''
        Endpoint for transcribing audio files
    '''
    print(audio.content_type)
    audio_codec = audio.content_type.split("/")[-1] if "/" in audio.content_type else None

    print(audio_codec)
    audio_bytes = audio.file.read()
    audio_properties = get_audio_properties(audio_bytes)

    if audio_properties.get('frame_rate') != 16000:
        audio_bytes = convert_audio_compatibility(audio_bytes)

    audio_array = np.frombuffer(audio_bytes, np.int16).astype(np.float32).flatten() / 32768.0

    transcription = model.transcribe(
        audio_array, 
        language="es", 
        fp16=False, 
        verbose=True,
    )
    transcription['text'] = transcription['text'].strip()

    return transcription
