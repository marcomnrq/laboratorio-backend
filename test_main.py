from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_endpoint_rechazo():
    response = client.get("/evaluar?edad=17&ingresos=2000")
    assert response.status_code == 200
    assert response.json()["status"] == "RECHAZADO"

def test_endpoint_regular():
    response = client.get("/evaluar?edad=22&ingresos=3000")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "OK"
    assert body["data"]["categoria"] == "Tarjeta OH"

def test_endpoint_premium():
    response = client.get("/evaluar?edad=30&ingresos=6000")
    assert response.status_code == 200
    body = response.json()
    assert body["data"]["categoria"] == "Tarjeta OH Premium"

def test_endpoint_datos_invalidos():
    response = client.get("/evaluar?edad=-5&ingresos=1000")
    assert response.status_code == 400
    assert response.json()["detail"] == "Datos inválidos"
