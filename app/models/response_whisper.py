from pydantic import BaseModel



class Segment(BaseModel):
    id:int
    seek:int
    start:float
    end:float
    text:str
    tokens: list[int]
    temperature:float
    avg_logprob:float
    compression_ratio:float
    no_speech_prob:float

class ResponseWhisper(BaseModel):
    text:str
    segments:list[Segment]
    language:str