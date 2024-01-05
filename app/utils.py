from pydub import AudioSegment
import io
import ffmpeg
import subprocess
import json

from .models.audio_format import (
    AudioProperties
)

from pprint import pprint

def get_audio_properties(audio_bytes: bytes) -> AudioProperties:
    '''
        Function to extract audio properties

        This function is build considering th ffmpeg package
        https://github.com/kkroening/ffmpeg-python/blob/master/ffmpeg/_probe.py
        
        and adapt to get the properties in json format using a pipe 
    '''

    cmd = [
        'ffprobe',
        "-hide_banner",
        '-show_format', 
        '-i', 'pipe:0',
        '-show_streams', '-of', 'json'
    ]
    
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    stdout, stderr = process.communicate(input=audio_bytes)

    try:
        properties = json.loads(
            stdout
        )

        return AudioProperties(
            **properties
        )
    
    except Exception as e:
        raise RuntimeError(f"Error extracting audio properties: {str(e)}")


def convert_audio_compatibility(audio_bytes:bytes) -> bytes:
    '''
        Function to convert audio to a compatible format

        Args:
            audio_bytes: bytes of audio file

        Returns:
            bytes: bytes of audio file converted
    
    '''
    audio_format = "wav"
    target_sample_width = 2  # 16-bit (2 bytes)
    target_channels = 1  # Mono audio
    target_frame_rate = 16000  # 16 kHz sample rate

    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    audio = audio.set_sample_width(target_sample_width)
    audio = audio.set_channels(target_channels)
    audio = audio.set_frame_rate(target_frame_rate)

    # Convert audio data to bytes with the target format
    output_buffer = io.BytesIO()
    audio.export(output_buffer, format=audio_format)

    return output_buffer.getvalue()

