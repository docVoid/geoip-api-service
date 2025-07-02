from pydantic import BaseModel
from typing import Optional

class GeoInfo(BaseModel):
    latitude: float
    longitude: float
    time_zone: Optional[str]

class GeoIPResponse(BaseModel):
    api_version: str
    ip: str
    geo: GeoInfo
    time: int