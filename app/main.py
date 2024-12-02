from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    """
    Handles the root endpoint of the application.

    Returns:
        JSONResponse: A JSON response containing a message with a placeholder for a password.
    """
    msg = JSONResponse(content={"contraseña": "Enserio pensaron que iba a poner la contraseña aquí?"},
                       status_code=200)
    return msg


@app.middleware("http")
async def check_user(request: Request, call_next):
    """
    Middleware to check the user from the request headers.

    Args:
        request (Request): The incoming HTTP request.
        call_next (Callable): The next middleware or route handler to call.

    Returns:
        Response: The HTTP response. If the user is "SosaDevLab", the request is passed to the next handler.
                  Otherwise, a JSON response with an error message and a 401 status code is returned.
    """
    user = request.headers.get("X-User")
    if user == "SosaDevLab":
        response = await call_next(request)
    else:
        response = JSONResponse(content={"error": "Bro???"}, status_code=401)
    return response
