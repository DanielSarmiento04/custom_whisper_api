from . import app
import whisper
from fastapi import (
    UploadFile
)
from .utils import(
    get_audio_properties,
    convert_audio_compatibility
)
import numpy as np
import logging

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
def transcribe(
        audio:UploadFile,
        language:str="es",
        # language_to:str="en",
    ):
    '''
        Endpoint for transcribing audio files
    '''
    logging.info(f"Transcribing audio with content type: {audio.content_type}")

    audio_codec = audio.content_type.split("/")[-1] if "/" in audio.content_type else None
    logging.info(f"Audio codec: {audio_codec}")

    audio_bytes = audio.file.read()
    audio_properties = get_audio_properties(audio_bytes)
    
    logging.info(f"Audio properties: {audio_properties}")
    if audio_properties.get('codec_name') != 'pcm_s16le':
        logging.warning(f"Audio codec not supported: {audio_properties.get('codec_name')}")
        audio_bytes = convert_audio_compatibility(audio_bytes)

    audio_array = np.frombuffer(audio_bytes, np.int16).astype(np.float32).flatten() / 32768.0

    transcription = model.transcribe(
        audio_array, 
        language=language, 
        # fp16=False, 
        verbose=True,
    )
    transcription['text'] = transcription['text'].strip()

    return transcription

