"""Pruebas del cálculo de inventario."""
import pytest

from src.inventario import dias_de_inventario, necesita_reposicion


def test_dias_normales():
    # 100 unidades, 10 por día -> 10 días
    assert dias_de_inventario(100, 10) == 10


def test_sin_ventas_dura_infinito():
    # sin ventas, devolvemos -1 (señal de "no se acaba")
    assert dias_de_inventario(50, 0) == -1.0


def test_necesita_reposicion_true():
    # 20 unidades, 10 por día -> 2 días < 7 -> sí necesita
    assert necesita_reposicion(20, 10) is True


def test_no_necesita_reposicion():
    # 100 unidades, 10 por día -> 10 días > 7 -> no necesita
    assert necesita_reposicion(100, 10) is False


def test_stock_negativo_lanza_error():
    with pytest.raises(ValueError):
        dias_de_inventario(-5, 10)
