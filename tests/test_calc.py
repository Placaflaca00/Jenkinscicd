import pytest
from app.calc import add

def test_add():
    assert add(2, 3) == 5  # Esta prueba debería pasar

@pytest.mark.xfail(reason="Intentional failure for testing pipeline behavior")
def test_add_failure():
    assert add(2, 3) == 6  # Esta prueba está diseñada para fallar
