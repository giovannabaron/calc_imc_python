import pytest
from imc import calcular_imc, classificar_imc

def test_calculo_basico():
    assert round(calcular_imc(70, 1.75), 2) == 22.86

def test_altura_zero():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_classificacao_normal():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificacao_sobrepeso():
    assert classificar_imc(27.0) == "Sobrepeso"

def test_classificacao_obesidade():
    assert classificar_imc(35.0) == "Obesidade grau 2"