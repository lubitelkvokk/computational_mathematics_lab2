def calculate_x(x_i, func, first_derivatative_func):
    return x_i - func(x_i) / first_derivatative_func(x_i)


def derivative_of_polynom(koeffs):
    new_koeffs = []
    for i in range(1, len(koeffs)):
        new_koeffs.append(koeffs[i] * i)
    return new_koeffs


def find_solution(a: float, b: float, koeffs, accuracy: float):

    first_derivatative_new_koeffs = derivative_of_polynom(koeffs)
    second_derivatative_new_koeffs = derivative_of_polynom(first_derivatative_new_koeffs)

    func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(koeffs))
    first_derivatative_func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(first_derivatative_new_koeffs))
    second_derivative_func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(second_derivatative_new_koeffs))
    if func(a) * second_derivative_func(a) > 0:
        x_i = a
    else:
        x_i = b

    x_i = calculate_x(x_i, func, first_derivatative_func)

    iteration_count = 1
    while abs(func(x_i)) > accuracy:
        iteration_count += 1
        x_i = calculate_x(x_i, func, first_derivatative_func)

    return x_i, iteration_count


# print(find_solution(-2, -1, function, 0.01))
