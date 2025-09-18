from typing import Callable


def integrate(f: Callable[[float], float], a: float, b: float, n: int = 1000):
    h = (b - a) / n
    integral = 0.0
    for i in range(n):
        x = a + i * h
        integral += f(x)
    return integral * h
