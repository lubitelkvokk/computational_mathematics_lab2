from sympy import sin, symbols, diff


def calculate_x(x, x_i, func, first_derivatative_func):
    return x_i - func(x_i) / first_derivatative_func.subs(x, x_i)


def derivative_of_polynom(koeffs):
    new_koeffs = []
    for i in range(1, len(koeffs)):
        new_koeffs.append(koeffs[i] * i)
    return new_koeffs


def find_solution(a: float, b: float, func, accuracy: float):
    x = symbols('x')
    sympy_func = func(x)

    first_derivatative_func = diff(sympy_func, x)
    second_derivative_func = diff(sympy_func, x, 2)

    if func(a) * second_derivative_func.subs(x, a) > 0:
        x_i = a
    else:
        x_i = b

    x_i = calculate_x(x, x_i, func, first_derivatative_func)

    iteration_count = 1
    while abs(func(x_i)) > accuracy:
        iteration_count += 1
        x_i = x_i = calculate_x(x, x_i, func, first_derivatative_func)

    return x_i, iteration_count

# print(find_solution(-2, -1, function, 0.01))
