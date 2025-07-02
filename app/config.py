import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


GEOIP_DB_PATH = os.path.join(BASE_DIR, "GeoLite2-City.mmdb")
API_VERSION = "1.0.0"