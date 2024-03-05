import io
import numpy as np
from matplotlib import pyplot as plt


def generate_plot(koeffs, left_board, right_board, accuracy):
    x = np.linspace(left_board, right_board, 1000)
    y = sum(koeff * x ** i for i, koeff in enumerate(koeffs))
    # Создание графика
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y)

    # Добавление линий осей
    ax.axhline(0, color='black', linewidth=0.5)  # Горизонтальная линия оси Y
    ax.axvline(0, color='black', linewidth=0.5)  # Вертикальная линия оси X

    ax.grid(True)
    plt.savefig("static/images/image.png")
    # Очистка графика из памяти, чтобы освободить ресурсы
    plt.close(fig)
