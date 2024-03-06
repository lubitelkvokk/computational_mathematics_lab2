from numpy import copy


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


def value_of_polynom(koeffs, x):
    sm = 0
    for i in range(len(koeffs)):
        sm += (x ** i) * koeffs[i]
        print((x ** i) * koeffs[i])
    return sm


def find_solution(a: float, b: float, koeffs, accuracy: float):
    primary_koeff = copy(koeffs)
    func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(primary_koeff))

    derivative_koeffs = derivative_of_polynom(koeffs)

    derivative_func_a = value_of_polynom(derivative_koeffs, a)
    derivative_func_b = value_of_polynom(derivative_koeffs, b)

    if (derivative_func_a > 0 and derivative_func_b > 0):
        lmbd = -1 / max(abs(derivative_func_a), abs(derivative_func_b))
    else:
        lmbd = 1 / max(abs(derivative_func_a), abs(derivative_func_b))

    koeffs = [k * lmbd for k in koeffs]
    koeffs[1] += 1

    phi_func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(koeffs))

    x_i = a if abs(derivative_func_a) > abs(derivative_func_b) else b

    iteration_count = 0
    diff = 999
    while abs(func(x_i)) > accuracy or abs(diff) > accuracy:
        iteration_count += 1
        new_x = phi_func(x_i)
        diff = x_i - new_x
        x_i = new_x
        print(f"x_{iteration_count}", x_i)
        print(f"f({x_i})={func(x_i)}")
        if (iteration_count > 100):
            raise Exception(
                f"too many iterations, phi func values {[1 + derivative_func_a * lmbd, 1 + derivative_func_b * lmbd]}")

    return x_i, iteration_count, [1 + derivative_func_a * lmbd, 1 + derivative_func_b * lmbd]
