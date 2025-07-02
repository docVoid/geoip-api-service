import pytest
from httpx import AsyncClient
from app.main import app


VALID_IP = "125.45.67.18"
INVALID_IP = "999.999.999.999"
UNKNOWN_IP = "192.0.2.1"  # reserved IP that won't be in DB

@pytest.mark.asyncio
async def test_valid_ip():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/{VALID_IP}")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["ip"] == VALID_IP
    assert "latitude" in json_data["geo"]
    assert "longitude" in json_data["geo"]
    assert "time_zone" in json_data["geo"]
    assert isinstance(json_data["time"], int)

@pytest.mark.asyncio
async def test_invalid_ip_format():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/{INVALID_IP}")
    assert response.status_code == 422  # FastAPI validation error

@pytest.mark.asyncio
async def test_unknown_ip():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/{UNKNOWN_IP}")
    assert response.status_code == 404
    assert response.json()["detail"] == "IP address not found in database"
