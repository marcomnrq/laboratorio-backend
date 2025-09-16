from fastapi import FastAPI, HTTPException
from scoring import evaluar_cliente

app = FastAPI()

# Endpoint para evaluar tarjetas de crédito
@app.get("/evaluar")
def evaluar(edad: int, ingresos: float):
    if edad < 0 or ingresos < 0:
        raise HTTPException(status_code=400, detail="Datos inválidos")

    resultado = evaluar_cliente(edad, ingresos)

    if resultado["aprobado"]:
        return {
            "status": "OK",
            "mensaje": f"Aprobado con {resultado['categoria']}",
            "data": resultado,
        }
    else:
        return {
            "status": "RECHAZADO",
            "mensaje": "No cumple requisitos para obtener tarjeta",
            "data": resultado,
        }
