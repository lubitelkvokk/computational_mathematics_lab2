from src.util.chord_method import find_solution as find_solution_with_chord_method
from src.util.newton_method import find_solution as find_solution_with_newton_method
from src.util.simple_iteration_method import find_solution as find_solution_with_simple_iteration_method
from src.util.isolation_intervals import get_isolation_intervals


def get_roots_intervals(a: float, b: float, step: float, func):
    intervals = get_isolation_intervals(a, b, step, func)
    return intervals


def get_roots_number(a: float, b: float, step: float, func):
    return len(get_roots_intervals(a, b, step, func))


def solve_with_chords(a: float, b: float, func, accuracy: float):
    # func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(koeffs))
    intervals = get_roots_intervals(a, b, 1, func)
    result = ""
    if len(intervals) == 0:
        result += "There are no roots on this interval"
        return result
    else:
        root_number = 0
        result += f"Found roots:\n"
        for i in intervals:
            root_number += 1
            x_i, iteration_count = find_solution_with_chord_method(i[0], i[1], func, accuracy)
            result += f"{root_number} root: f({x_i}) = {func(x_i)}, iteration count: {iteration_count}, start interval: {i}\n"
        return result


def solve_with_newton(a: float, b: float, func, accuracy: float):
    # func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(koeffs))
    intervals = get_roots_intervals(a, b, 0.1, func)
    result = ""
    if len(intervals) == 0:
        result += "There are no roots on this interval"
        return result
    else:
        root_number = 0
        result += f"Found roots:\n"
        for i in intervals:
            root_number += 1
            x_i, iteration_count, x_0, derivative_values = find_solution_with_newton_method(i[0], i[1], func, accuracy)
            result += f"{root_number} root: f({x_i}) = {func(x_i)}, iteration count: {iteration_count}," \
                      f" x0={x_0}, derivative values: {derivative_values}\n" \
                      f"--------------------------------------------------------"
        return result


def solve_with_simple_iteration(a: float, b: float, koeffs, accuracy: float):
    func = lambda x: sum(koeff * x ** i for i, koeff in enumerate(koeffs))
    intervals = get_roots_intervals(a, b, 1, func)
    result = ""

    if len(intervals) == 0:
        result += "There are no roots on this interval"
        return result
    else:
        root_number = 0
        result += f"Found roots:\n"
        for i in intervals:
            root_number += 1
            x_i, iteration_count, phi_values = find_solution_with_simple_iteration_method(i[0], i[1], koeffs, accuracy)
            result += f"{root_number} root: f({x_i}) = {func(x_i)}, iteration count: {iteration_count}," \
                      f" iteration count: {iteration_count}, start interval: {i}," \
                      f"{phi_values}\n"
        return result
