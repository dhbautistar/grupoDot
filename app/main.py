from fastapi import FastAPI 
from dotenv import load_dotenv
from .routes.auth import auth_routes
from .routes.palindromo import palindromo

app = FastAPI()
app.include_router(auth_routes, prefix="/api")
app.include_router(palindromo, prefix="/api")

@app.get("/")
def read_root():
    return {"Endpoint general"}

load_dotenv()
