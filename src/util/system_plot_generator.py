# import numpy as np
# import matplotlib.pyplot as plt
#
# def func1(x, y):
#     return 1.5 * x - np.sin(x + y) - 0.1
#
# def func2(x, y):
#     return x ** 2 + 2 * y ** 2 - 1
#
# def generate_system_plot(func1, func2, left_board, right_board, accuracy):
#     x = np.linspace(left_board, right_board, 1000)
#     y = np.linspace(left_board, right_board, 1000)
#     X, Y = np.meshgrid(x, y)
#     Z1 = func1(X, Y)
#     Z2 = func2(X, Y)
#
#     fig, ax = plt.subplots(figsize=(10, 5))
#     # Отображение контуров функций
#     contour1 = ax.contour(X, Y, Z1, levels=[0], colors='blue', alpha=0.5)
#     contour2 = ax.contour(X, Y, Z2, levels=[0], colors='red', alpha=0.5)
#
#     ax.grid(True)
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_title('System of Functions')
#     ax.legend(['Func1', 'Func2'])
#
#     plt.savefig("image.png")
#     plt.close(fig)
#
# # Пример использования функции generate_system_plot
# generate_system_plot(func1, func2, -5, 5, 0.01)

import sympy as sp
from math import sin
# Создайте символьную переменную
x = sp.symbols('x')

# Определите функцию
func = "arctan(x)"

# Вычислите n-ую производную
n = 1  # Замените на необходимое значение n
# derivative = sp.diff(func, x, n)

# Выведите результат
print(sp.solve(sin(x), x))