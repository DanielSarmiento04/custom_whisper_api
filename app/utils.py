from pydub import AudioSegment
import io
import ffmpeg
import subprocess
import json

def get_audio_properties(audio_bytes: bytes):
    '''
        Function to extract audio properties

        This function is build considering th ffmpeg package
        https://github.com/kkroening/ffmpeg-python/blob/master/ffmpeg/_probe.py
        
        and adapt to get the properties in json format using a pipe 
    '''
    try:
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
        properties = stderr.decode("utf-8")

        return json.loads(stdout).get("streams")[0]
    except Exception as e:
        raise RuntimeError(f"Error extracting audio properties: {str(e)}")


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

def convert_video_to_audio(video_bytes: bytes):
    '''
        Function to convert video to audio

    '''

    video_manipulated = video_bytes

    pipe = ffmpeg.input("pipe:0", threads=0)
    pipe = ffmpeg.output(pipe, "pipe:1", format="s16le", acodec="pcm_s16le", ac=1, ar="16k")
    video_manipulated, _ = pipe.run(input=video_manipulated, capture_stdout=True, capture_stderr=True)