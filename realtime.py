import pyaudio
import asyncio
import websockets
import os
import json


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000
CHUNK = 8000


audio_queue = asyncio.Queue()

def callback(input_data, frame_count, time_info, status_flags):
   
   audio_queue.put_nowait(input_data)

   return (input_data, pyaudio.paContinue)


async def microphone(): 
   
   audio = pyaudio.PyAudio()
   stream = audio.open(
       format = FORMAT,
       channels = CHANNELS,
       rate = RATE,
       input = True,
       frames_per_buffer = CHUNK,
       stream_callback = callback
   )

   stream.start_stream()

   while stream.is_active():
       await asyncio.sleep(0.1)


   stream.stop_stream()
   stream.close()



async def process():

   async with websockets.connect(
        'ws://localhost:8000/ws', 
       ) as ws:
       async def sender(ws): # sends audio to websocket
           
           
           try:
               while True:
                   data = await audio_queue.get()
                   await ws.send(data)
           except Exception as e:
               print('Error while sending: ', + str(e))
               raise

       async def receiver(ws): 
           async for msg in ws:
               msg = json.loads(msg)
               transcript = msg['channel']['alternatives'][0]['transcript']

               if transcript:
                   print(f'Transcript = {transcript}')

       await asyncio.gather(sender(ws), receiver(ws))

      
async def run():
   
   await asyncio.gather(microphone(),process())

if __name__ == '__main__':
   asyncio.run(run())