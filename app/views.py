from . import app
import whisper
from fastapi import (
    UploadFile,
    WebSocket
)
from .utils import(
    get_audio_properties,
    convert_audio_compatibility
)
import numpy as np
import logging
from .constants import (
    ALLOW_CODEC,
    ALLOW_EXTENSIONS,
    AudioWS
)

from .exceptions import (
    NoAllowExtensionException
)

from .models import (
    AudioProperties,
    ResponseWhisper,
    Language
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
    response_model=AudioProperties,
)
def audio_properties(
        audio:UploadFile,
    ):
    '''
        Endpoint for get properties audio files

        Parameters
        ----------

        audio: UploadFile
            Audio file to transcribe
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
        language:Language = Language.es
    ):
    '''
        Endpoint for transcribing audio files

        Parameters
        ----------

        audio: UploadFile
            Audio file to transcribe
        
        language: Language
            Language of the audio file

        Returns
        -------
        ResponseWhisper
            Object with the transcription of the audio file
    '''
    logging.info(f"Transcribing audio with content type: {audio.content_type}")

    extension = audio.content_type.split("/")[-1]

    if not (extension in ALLOW_EXTENSIONS):
        raise NoAllowExtensionException(f"Extension not allowed: {extension}")
    
    audio_bytes = audio.file.read()
    audio_properties = get_audio_properties(audio_bytes)

    if  audio_properties.streams[0].codec_name  != ALLOW_CODEC or \
        audio_properties.streams[0].sample_rate != 8000:
        
        logging.warning(f"Audio codec not supported: {audio_properties.streams[0].codec_name}")
        audio_bytes = convert_audio_compatibility(audio_bytes)

    audio_array = np.frombuffer(audio_bytes, np.int16).astype(np.float32).flatten() / 32768.0

    transcription = model.transcribe(
        audio_array, 
        language=language.value, 
        verbose=True,
    )

    transcription['text'] = transcription['text'].strip()

    return ResponseWhisper(
        **transcription
    )



@app.websocket(
    path='/ws'
)
async def websocket(
    websocket:WebSocket, 
    sample_rate:int, 
    language:str
):
    '''
        Websocket connection
    
    '''
    
    await websocket.accept()


    try:
        while True:

            audio_bytes:bytes = await websocket.receive_bytes()

            audio_array = np.frombuffer(audio_bytes, np.int16).astype(np.float32).flatten() / 32768.0

            transcription = model.transcribe(
                audio_array, 
                language=language, 
                verbose=True,
            )
            print(transcription)

    except Exception as e:
        logging.error(e)
        # if websocket.s
        # await websocket.close()




