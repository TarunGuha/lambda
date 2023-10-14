from fastapi import APIRouter

from app.services.news.routers.routes import router as news_router

router = APIRouter()

router.include_router(news_router,prefix='/news-service')