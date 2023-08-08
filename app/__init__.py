from fastapi import FastAPI
from colorama import Fore

app = FastAPI()

from .views import *

logging.basicConfig(
    level=logging.INFO,
    format=fr'{Fore.LIGHTBLUE_EX}%(levelname)s {Fore.RESET} %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ],
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.basicConfig(
    level=logging.WARNING,
    format=fr'{Fore.LIGHTCYAN_EX}%(levelname)s {Fore.RESET} %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ],
    datefmt='%Y-%m-%d %H:%M:%S'
)