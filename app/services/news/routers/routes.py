from fastapi import APIRouter
from app.services.news.routers.models import stations
from app.services.news.interactions.list_stations import list_stations

router = APIRouter()

@router.get("/")
def root_news():
    return { 'health' : 'ok' }

@router.post("/list_stations")
def call_list_stations(stations:stations):
    return list_stations(stations)