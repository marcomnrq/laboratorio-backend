def evaluar_cliente(edad: int, ingresos: float) -> dict:
    if edad < 18 or ingresos < 1000:
        return {"aprobado": False, "categoria": None, "linea": 0}

    if ingresos < 5000:
        return {"aprobado": True, "categoria": "Tarjeta OH", "linea": 2000}

    if ingresos >= 50000 and edad >= 25:
        return {"aprobado": True, "categoria": "Tarjeta OH Premium", "linea": 10000}

    return {"aprobado": True, "categoria": "Tarjeta OH", "linea": 2000}
