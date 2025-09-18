from function import add_numbers
from integrator import integrate


def f(x):
    return x * x + 1


def main():
    # Adding numbers:
    print(add_numbers(10, 10))

    # Rectangle Integral:
    res = integrate(f, 0, 10)
    print(res)


if __name__ == '__main__':
    main()
