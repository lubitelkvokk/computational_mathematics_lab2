def calculate_x(a_i, b_i, func):
    return (a_i * func(b_i) - b_i * func(a_i)) / (func(b_i) - func(a_i))


def find_solution(a: float, b: float, func, accuracy: float):
    a_i, b_i = a, b

    x_i = calculate_x(a_i, b_i, func)

    iteration_count = 1
    while abs(func(x_i)) > accuracy:
        iteration_count += 1
        if func(x_i) * func(a_i) < 0:
            b_i = x_i
        else:
            a_i = x_i
        x_i = calculate_x(a_i, b_i, func)
        if (iteration_count > 100):
            raise Exception("too many iterations")

    return x_i, iteration_count


def function(x):
    return x ** 3 - x + 4


# print(find_solution(-2, -1, function, 0.01))
