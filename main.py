from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Fast API Working"}

handler = Mangum(app)