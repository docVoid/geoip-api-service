import pytest
from httpx import AsyncClient
from app.main import app
from fastapi import FastAPI

@pytest.mark.asyncio
async def test_valid_ip():
    async with AsyncClient(base_url="http://test", transport=None, app=app) as ac:
        response = await ac.get("/125.45.67.18")
    assert response.status_code == 200
    data = response.json()
    assert "latitude" in data["geo"]
    assert "longitude" in data["geo"]

@pytest.mark.asyncio
async def test_invalid_ip_format():
    async with AsyncClient(base_url="http://test", transport=None, app=app) as ac:
        response = await ac.get("/999.999.999.999")
    assert response.status_code == 422  # validation error

@pytest.mark.asyncio
async def test_unknown_ip():
    async with AsyncClient(base_url="http://test", transport=None, app=app) as ac:
        response = await ac.get("/192.0.2.1")
    assert response.status_code == 404
