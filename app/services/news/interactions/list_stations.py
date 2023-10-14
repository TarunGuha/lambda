from app.services.news.constants.list_stations_constants import BENGALI_STATIONS,HINDI_STATIONS

def list_stations(data):
    if data.language == 'hindi':
        return HINDI_STATIONS
    if data.language == 'bengali':
        return BENGALI_STATIONS
    return []