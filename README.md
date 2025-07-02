# 🌍 geoip-api-service

Get GeoIP information with an API call.

[![Latest version](https://badgen.net/github/release/docVoid/geoip-api-service)](https://github.com/docVoid/geoip-api-service/releases) [![License](https://badgen.net/github/license/docVoid/geoip-api-service)](https://github.com/docVoid/geoip-api-service/LICENSE)

---

This is a simple and fast IP geolocation API built with FastAPI and the MaxMind GeoLite2 City database. You can query IP addresses and get their geographic location (latitude, longitude, and time zone) via a single HTTP call.


## 🚀 Features

- FastAPI-based REST API
- Local IP geolocation using MaxMind's GeoLite2 City database
- JSON response with coordinates, timezone, and timestamp
- Docker support
- Easy deployment on localhost or server

---

## 📦 Requirements

- Python 3.11+
- MaxMind GeoLite2 City database (`GeoLite2-City.mmdb`)
- A MaxMind account (free) to download the DB:  
  https://www.maxmind.com/en/geolite2/signup

---

## 🔧 Installation

```bash
git clone https://github.com/your-username/geoip-api-service.git
cd geoip-api-service
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:  
http://127.0.0.1:8000

---

## 📡 Example Request

```bash
curl http://localhost:8000/125.45.67.18
```

### ✅ Response

```json
{
  "api_version": "1.0.0",
  "ip": "125.45.67.18",
  "geo": {
    "latitude": 34.6836,
    "longitude": 113.5325,
    "time_zone": "Asia/Shanghai"
  },
  "time": 1720153200
}
```

---

## 📁 Project Structure

```plaintext
geoip-api-service/
├── app/
│   ├── main.py          # API entrypoint
│   ├── api.py           # Route definitions
│   ├── geoip.py         # GeoIP lookup logic
│   ├── config.py        # Configuration
│   ├── schemas.py       # Response models
│   └── GeoLite2-City.mmdb  # Database
├── tests/               # Tests
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```


---


Feel free to open issues or pull requests to contribute!