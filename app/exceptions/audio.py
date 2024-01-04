from .. import app
from fastapi import Request
from fastapi.responses import JSONResponse
from colorama import Fore


class NoAllowExtensionException(Exception):
    """
        Class used to raise a no use found user in the database
    """
    def __init__(self, extension: str):

        self.extension = extension


@app.exception_handler(NoAllowExtensionException)
async def no_allow_exception_exception(request: Request, exc: NoAllowExtensionException):
    '''
        No allow exceptions handler
    '''

    print(Fore.LIGHTCYAN_EX, f"No allow exception {exc.extension}", Fore.RESET)
    
    return JSONResponse(
        status_code=406,
        content={"detail": f"Extension {exc.extension} not allowed"},
        headers={"Content-Type": "application/json"},
    )

