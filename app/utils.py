from pydub import AudioSegment
import io
import ffmpeg

def get_audio_properties(audio_bytes:bytes):
    '''
        Function to extract audio properties
    '''
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    duration_ms = len(audio)
    channels = audio.channels
    frame_rate = audio.frame_rate
    sample_width = audio.sample_width
    return {
        "duration_ms": duration_ms,
        "channels": channels,
        "frame_rate": frame_rate,
        "sample_width": sample_width,
    }

def convert_audio_compatibility(audio_bytes:bytes):
    '''
        Function to convert audio to a compatible format
    '''
    audio_manipulated = audio_bytes
    # convert from mp4a to pcm_s16le 
    pipe = ffmpeg.input("pipe:0", threads=0)
    pipe = ffmpeg.output(pipe, "pipe:1", format="s16le", acodec="pcm_s16le", ac=1, ar="16k")
    audio_manipulated, _ = pipe.run(input=audio_manipulated, capture_stdout=True, capture_stderr=True)

    return audio_manipulated