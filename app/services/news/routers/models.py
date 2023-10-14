from pydantic import BaseModel

class stations(BaseModel):
    language: str

class livestreams(BaseModel):
    station_handle: str