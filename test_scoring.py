from scoring import evaluar_cliente

def test_rechazo_por_edad():
    result = evaluar_cliente(17, 2000)
    assert result["aprobado"] is False

def test_rechazo_por_ingresos():
    result = evaluar_cliente(25, 800)
    assert result["aprobado"] is False

def test_tarjeta_oh_regular():
    result = evaluar_cliente(22, 3000)
    assert result["aprobado"] is True
    assert result["categoria"] == "Tarjeta OH"

def test_tarjeta_oh_premium():
    result = evaluar_cliente(30, 6000)
    assert result["aprobado"] is True
    assert result["categoria"] == "Tarjeta OH Premium"

def test_tarjeta_oh_regular_por_edad():
    # Cliente gana mucho pero es menor de 25 años, no accede a Premium
    result = evaluar_cliente(22, 6000)
    assert result["aprobado"] is True
    assert result["categoria"] == "Tarjeta OH"
    assert result["linea"] == 2000
