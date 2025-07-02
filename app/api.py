from fastapi import APIRouter
from datetime import datetime
from . import geoip, schemas, config

router = APIRouter()

@router.get("/{ip_address}", response_model=schemas.GeoIPResponse)
def get_geoip_info(ip_address: str):
    geo_data = geoip.lookup_ip(ip_address)
    timestamp = int(datetime.utcnow().timestamp())
    
    return schemas.GeoIPResponse(
        api_version=config.API_VERSION,
        ip=ip_address,
        geo=schemas.GeoInfo(**geo_data),
        time=timestamp
    )
