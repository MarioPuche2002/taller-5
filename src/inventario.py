"""Cálculo de reposición de inventario para una cadena de tiendas."""

def dias_de_inventario(stock_actual: int, ventas_diarias: float) -> float:
    """Cuántos días durará el stock al ritmo de ventas actual.

    Si no hay ventas, el stock dura 'infinito' (devolvemos -1 como señal).
    """
    if stock_actual < 0:
        raise ValueError("stock_actual no puede ser negativo")
    if ventas_diarias < 0:
        raise ValueError("ventas_diarias no puede ser negativo")
    if ventas_diarias == 0:
        return -1.0
    return stock_actual / ventas_diarias


def necesita_reposicion(stock_actual: int, ventas_diarias: float, umbral_dias: int = 7) -> bool:
    """True si el stock se acaba antes del umbral de días."""
    dias = dias_de_inventario(stock_actual, ventas_diarias)
    if dias == -1.0:
        return False
    return dias < umbral_dias
