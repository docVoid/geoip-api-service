import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from app.main import app

transport = ASGITransport(app=app, raise_app_exceptions=True)

@pytest.mark.asyncio
async def test_valid_ip():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/125.45.67.18")
    assert response.status_code == 200
    data = response.json()
    assert "latitude" in data["geo"]
    assert "longitude" in data["geo"]

@pytest.mark.asyncio
async def test_invalid_ip_format():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/999.999.999.999")
    assert response.status_code == 422  # FastAPI's validation

@pytest.mark.asyncio
async def test_unknown_ip():
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/192.0.2.1")
    assert response.status_code == 404
    assert response.json()["detail"] == "IP address not found in database"
