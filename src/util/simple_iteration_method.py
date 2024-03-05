def calculate_x(x_i, func, first_derivatative_func):
    return x_i - func(x_i) / first_derivatative_func(x_i)


def koeffs_after_x_expression(koeffs):
    koeffs[1] += 1
    return koeffs


def derivative_of_polynom(koeffs):
    new_koeffs = []
    for i in range(1, len(koeffs)):
        new_koeffs.append(koeffs[i] * i)
    return new_koeffs


def find_solution(a: float, b: float, koeffs, accuracy: float):
    # koeffs = koeffs_after_x_expression(koeffs)
    # func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(koeffs))

    derivative_koeffs = derivative_of_polynom(koeffs)
    derivative_func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(derivative_koeffs))

    derivative_func_a = derivative_func(a)
    derivative_func_b = derivative_func(b)

    # if (derivative_func_a > 0 and derivative_func_b > 0):
    #     lmbd = -1 / max(derivative_func_a, derivative_func_b)
    # else:
    lmbd = 1 / max(derivative_func_a, derivative_func_b)

    # print(f"derivative_result_a:{a}, b:{b}")
    print("lambda", lmbd)
    koeffs = [k * lmbd for k in koeffs]
    koeffs[1] += 1
    phi_func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(koeffs))

    # if derivative_func_a > 1 and derivative_func_b > 1:
    #     raise Exception("Условие сходимости не выполняется")

    if abs(derivative_func_a) < abs(derivative_func_b):
        x_i = a
    else:
        x_i = b

    # print(koeffs)
    # print("ABOBA")
    print("x_0", x_i)

    iteration_count = 1
    diff = 999
    while abs(diff) > accuracy:
        iteration_count += 1
        new_x = phi_func(x_i)
        diff = x_i - new_x
        x_i = new_x
        print(f"x_{iteration_count}", x_i)

    return x_i, iteration_count

# print(find_solution(-2, -1, function, 0.01))
