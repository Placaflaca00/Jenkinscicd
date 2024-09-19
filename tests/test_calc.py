from app.calc import add

def test_add():
    assert add(2, 3) == 5  # Esta prueba debería pasar
    assert add(2, 3) == 6  # Esta prueba debería fallar para ver cómo el pipeline detecta errores