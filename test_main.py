from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_non_weather_question():
    response = client.post("/", json={"message": "Qual era a principal guitarra do Jimi Hendrix?"})
    assert response.status_code == 200
    assert "Fender" in response.json()["response"]

def test_weather_question():
    response = client.post("/", json={"message": "Vai chover em São Paulo amanhã?"})
    assert response.status_code == 200
    assert "São Paulo" in response.json()["response"]
