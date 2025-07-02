import geoip2.database
from .config import GEOIP_DB_PATH
from fastapi import HTTPException

reader = geoip2.database.Reader(GEOIP_DB_PATH)

def lookup_ip(ip_address: str):
    try:
        response = reader.city(ip_address)
        return {
            "latitude": response.location.latitude,
            "longitude": response.location.longitude,
            "time_zone": response.location.time_zone
        }
    except geoip2.errors.AddressNotFoundError:
        raise HTTPException(status_code=404, detail="IP address not found in database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
