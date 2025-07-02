from fastapi import APIRouter
from pydantic import IPvAnyAddress
from datetime import datetime
from . import geoip, schemas, config

router = APIRouter()

@router.get("/{ip_address}", response_model=schemas.GeoIPResponse)
def get_geoip_info(ip_address: IPvAnyAddress): 
    geo_data = geoip.lookup_ip(str(ip_address))
    timestamp = int(datetime.utcnow().timestamp())
    
    return schemas.GeoIPResponse(
        api_version=config.API_VERSION,
        ip=str(ip_address),
        geo=schemas.GeoInfo(**geo_data),
        time=timestamp
    )

