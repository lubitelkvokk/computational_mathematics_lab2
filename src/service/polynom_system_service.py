from math import sin, cos


def solve_first_system(x: float, y: float, accuracy: float):
    x_i = x + accuracy * 2
    y_i = y + accuracy * 2
    x_new = x
    y_new = y
    result = ""
    iteration = 0

    result += f"Сходящийся процесс:\n"
    result += f"\t|d_phi_1/d_x| + |d_phi_1/d_y| = |0| + |sin({y - 2})| <= 1>\n"
    result += f"\t|d_phi_2/d_x| + |d_phi_2/d_y| = |cos({x + 0.5})| + |0| <= 1>\n"
    result += f"x_{iteration}={x_new}, y_{iteration}={y_new}\n"
    while abs(x_i - x_new) > accuracy or abs(y_i - y_new) > accuracy:
        x_i = x_new
        y_i = y_new
        x_new = -cos(y_i - 2)
        y_new = sin(x_i + 0.5) - 1
        iteration += 1
        result += f"x_{iteration} = {x_new},\ty_{iteration} = {y_new} \n"

    return f"iteration count {iteration}\n" + result


def solve_second_system(x: float, y: float, accuracy: float):
    x_i = x + accuracy * 2
    y_i = y + accuracy * 2
    x_new = x
    y_new = y
    result = ""
    iteration = 0
    result += f"Расходящийся процесс:\n"
    result += f"\t|d_phi_1/d_x| + |d_phi_1/d_y| = |-1| + |sin({y})| > 1\n"
    result += f"x_{iteration}={x_new}, y_{iteration}={y_new}\n"
    while abs(x_i - x_new) > accuracy or abs(y_i - y_new) > accuracy:
        x_i = x_new
        y_i = y_new
        x_new = 2 - cos(y_i) - x_i
        y_new = sin(x_i + 1) - 1.2
        iteration += 1
        result += f"x_{iteration} = {x_new},\ty_{iteration} = {y_new} \n"

    return f"iteration count {iteration}\n" + result
