import io
import numpy as np
from matplotlib import pyplot as plt


def generate_plot(func, left_board, right_board, accuracy):
    x = np.linspace(left_board, right_board, 1000)
    # y = k_for_x_3 * x ** 3 + k_for_x_2 * x ** 2 + k_for_x_1 * x + k_for_constant
    # Создание графика
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, [func(item) for item in x])

    # Добавление линий осей
    ax.axhline(0, color='black', linewidth=0.5)  # Горизонтальная линия оси Y
    ax.axvline(0, color='black', linewidth=0.5)  # Вертикальная линия оси X

    ax.grid(True)
    plt.savefig("static/images/system2.png")
    # Очистка графика из памяти, чтобы освободить ресурсы
    plt.close(fig)
