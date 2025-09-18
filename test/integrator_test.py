from src.integrator import integrate
import math


def test_integrate_simple():
    """integrate() basic assertion"""
    f = lambda x: x * x + 1
    assert math.isclose(integrate(f, 0, 10), 342.83350000000013)
    