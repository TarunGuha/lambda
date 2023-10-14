from fastapi import FastAPI
from app.core.config import APP_ENV

app = FastAPI()

if APP_ENV == 'production':
    from mangum import Mangum
    handler = Mangum(app)

@app.get("/")
async def root():
    return { "message": "Fast API Working"}