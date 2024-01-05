    # bit_rate:int
from pydantic import BaseModel


class Stream(BaseModel):
    
    avg_frame_rate:str
    codec_name:str
    codec_long_name:str
    codec_tag:str
    codec_tag_string:str
    codec_type:str
    initial_padding:int
    index:int 
    sample_fmt:str
    sample_rate:int
    channels:int
    bits_per_sample:int
    r_frame_rate:str

    time_base:str


class Tag(BaseModel):
    encoder:str


class Format(BaseModel):
    filename:str
    nb_streams:int
    nb_programs:int
    format_name:str
    format_long_name:str
    probe_score:int



class AudioProperties(BaseModel):

    streams:list[Stream]
    format:Format


