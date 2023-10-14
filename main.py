from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from mangum import Mangum

from app.routers.main_router import router as main_router

docs = {
    "title": "Lambda",
    "docs_url": "/docs"
}
app = FastAPI(**docs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return { "message": "Fast API Working"}

app.include_router(main_router)

handler = Mangum(app)