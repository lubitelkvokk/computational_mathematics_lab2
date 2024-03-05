from sympy import sympify, symbols

def create_lambda_function(expression_string):
    # Создаем символьную переменную
    x = symbols('x')

    # Преобразуем строку в символьное выражение
    symbolic_expression = sympify(expression_string)

    # Создаем и возвращаем лямбда-функцию
    return lambda x_value: symbolic_expression.subs(x, x_value)


