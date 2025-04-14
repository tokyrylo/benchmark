import pytest

from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_average_statistics():
    response = client.get("/results/average")
    assert response.status_code == 200
    assert "avg_token_count" in response.json()  

def test_get_average_statistics_by_time_window():
    response = client.get("/results/average/2024-06-01T00:00:00/2024-06-02T23:59:59")
    assert response.status_code == 200
    assert "avg_token_count" in response.json()
