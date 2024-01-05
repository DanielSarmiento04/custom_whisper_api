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
from .constants import (
    ALLOW_CODEC,
    ALLOW_EXTENSIONS
)

from .exceptions import (
    NoAllowExtensionException
)


from .models import (
    AudioProperties,
    ResponseWhisper
)

@app.get("/")
async def root():
    '''
        Base endpoint to test if the server is running
    '''
    return {"message": "Hello World"}

model = whisper.load_model(
    name="base"
)

@app.post(
    path="/get_audio_properties", 
    response_model=AudioProperties
)
def audio_properties(
        audio:UploadFile,
    ):
    '''
        Endpoint for get properties audio files
    '''  

    logging.info(f"Transcribing audio with content type: {audio.content_type}")

    extension = audio.content_type.split("/")[-1]

    if not (extension in ALLOW_EXTENSIONS):
        raise NoAllowExtensionException(f"Extension not allowed: {extension}")
    
    audio_bytes = audio.file.read()
    audio_properties = get_audio_properties(audio_bytes)
    
    return audio_properties


@app.post(
    path="/transcribe/",
    response_model=ResponseWhisper
)
def transcribe(
        audio:UploadFile,
        language:str="es",
    ):
    '''
        Endpoint for transcribing audio files
    '''
    logging.info(f"Transcribing audio with content type: {audio.content_type}")

    extension = audio.content_type.split("/")[-1]
    print(extension)

    if not (extension in ALLOW_EXTENSIONS):
        raise NoAllowExtensionException(f"Extension not allowed: {extension}")
    
    audio_bytes = audio.file.read()
    audio_properties = get_audio_properties(audio_bytes)

    if  audio_properties.streams[0].codec_name != ALLOW_CODEC or \
        audio_properties.streams[0].sample_rate != 8000:
        
        logging.warning(f"Audio codec not supported: {audio_properties.streams[0].codec_name}")
        audio_bytes = convert_audio_compatibility(audio_bytes)

    audio_array = np.frombuffer(audio_bytes, np.int16).astype(np.float32).flatten() / 32768.0

    transcription = model.transcribe(
        audio_array, 
        language=language, 
        # fp16=False, 
        verbose=True,
    )

    transcription['text'] = transcription['text'].strip()

    return ResponseWhisper(
        **transcription
    )
