from pydantic import BaseModel


# {
#     'text': ' Hola, bienvenido al Sistema de Supermercado Inteligente.', 
#     'segments': [
#         {
#             'id': 0, 
#             'seek': 0, 
#             'start': 0.0, 
#             'end': 3.0, 
#             'text': ' Hola, bienvenido al Sistema de Supermercado Inteligente.', 
#             'tokens': [50364, 22637, 11, 3610, 553, 2925, 419, 318, 468, 5619, 368, 4548, 936, 27713, 19762, 328, 1576, 13, 50514], 
#             'temperature': 0.0, 
#             'avg_logprob': -0.24760169982910157, 
#             'compression_ratio': 0.9180327868852459, 
#             'no_speech_prob': 0.03181925043463707
#         }
#     ], 
#     'language': 'es'
# }

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