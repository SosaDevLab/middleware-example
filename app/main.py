from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    msg = JSONResponse(content={"contraseña": "Enserio pensaron que iba a poner la contraseña aquí?"},
                       status_code=200)
    return msg


@app.middleware("http")
async def check_user(request: Request, call_next):
    user = request.headers.get("X-User")
    if user == "SosaDevLab":
        response = await call_next(request)
    else:
        response = JSONResponse(content={"error": "Bro???"}, status_code=401)
    return response
