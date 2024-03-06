from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from src.service.polynom_solver_service import solve_with_chords, solve_with_newton, solve_with_simple_iteration
from src.util.function_parser import create_lambda_function
from src.util.plot_generator import generate_plot

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/plot")
async def polynomial_solver(request: Request):
    default_values = {
        "request": request,
        'k_for_x_3': 0,
        'k_for_x_2': 0,
        'k_for_x_1': 0,
        'k_for_constant': 0,
        'left_board': -10,
        'right_board': 10,
        'accuracy': 0.01,
        'arbitrary_function': "sin(x)"
    }
    return templates.TemplateResponse("polynom_solver.html", default_values)


@router.post("/plot")
async def plot_graph(request: Request, k_for_x_3: float = Form(...), k_for_x_2: float = Form(...),
                     k_for_x_1: float = Form(...), k_for_constant: float = Form(...),
                     left_board: float = Form(...), right_board: float = Form(...),
                     accuracy: float = Form(...), method: str = Form(...)):
    func = create_lambda_function(f"{k_for_x_3}*x**3+{k_for_x_2}*x**2+{k_for_x_1}*x+{k_for_constant}")

    generate_plot(func, left_board, right_board, accuracy)

    print(method)
    try:
        if method == "chord":
            result = solve_with_chords(left_board, right_board,
                                       func,
                                       accuracy)
        elif method == "newton":

            result = solve_with_newton(left_board, right_board,
                                       func,
                                       accuracy)
        else:
            result = solve_with_simple_iteration(left_board, right_board,
                                                 [k_for_constant, k_for_x_1, k_for_x_2, k_for_x_3],
                                                 accuracy)
    except Exception as e:
        result = e

    return templates.TemplateResponse("polynom_solver.html",
                                      {
                                          "request": request,
                                          "plot_data": "static/images/image.png",
                                          "result": result,
                                          'k_for_x_3': k_for_x_3,
                                          'k_for_x_2': k_for_x_2,
                                          'k_for_x_1': k_for_x_1,
                                          'k_for_constant': k_for_constant,
                                          'left_board': left_board,
                                          'right_board': right_board,
                                          'accuracy': accuracy,
                                          'arbitrary_function': "sin(x)"
                                      })


@router.post("/arbitrary_function")
async def plot_graph_by_arbitrary_function(request: Request, arbitrary_function: str = Form(...),
                                           left_board: float = Form(...), right_board: float = Form(...),
                                           accuracy: float = Form(...), method: str = Form(...)):
    func = create_lambda_function(arbitrary_function)

    generate_plot(func, left_board, right_board, accuracy)

    print(method)
    try:
        if method == "chord":
            result = solve_with_chords(left_board, right_board,
                                       func,
                                       accuracy)
        elif method == "newton":
            result = solve_with_newton(left_board, right_board,
                                       func,
                                       accuracy)

    except Exception as e:
        result = e

    return templates.TemplateResponse("polynom_solver.html",
                                      {
                                          "request": request,
                                          "plot_data": "static/images/image.png",
                                          "result": result,
                                          'arbitrary_function': arbitrary_function,
                                          'left_board': left_board,
                                          'right_board': right_board,
                                          'accuracy': accuracy,
                                          'k_for_x_3': 0,
                                          'k_for_x_2': 0,
                                          'k_for_x_1': 0,
                                          'k_for_constant': 0,
                                      })

# @router.post("/polynom_system")
# async def plot_graph_by_polynom_system(request: Request, polynom1: str = Form(...), polynom2: str = Form(...),
#                                            left_board: float = Form(...), right_board: float = Form(...),
#                                            accuracy: float = Form(...), method: str = Form(...)):
#     func1 = create_lambda_function(polynom1)
#     func2 = create_lambda_function(polynom2)
#
#     generate_plot(func, left_board, right_board, accuracy)
#
#     print(method)
#     try:
#         if method == "chord":
#             result = solve_with_chords(left_board, right_board,
#                                        func,
#                                        accuracy)
#         elif method == "newton":
#             result = solve_with_newton(left_board, right_board,
#                                        func,
#                                        accuracy)
#
#     except Exception as e:
#         result = e
#
#     return templates.TemplateResponse("polynom_solver.html",
#                                       {
#                                           "request": request,
#                                           "plot_data": "static/images/image.png",
#                                           "result": result,
#                                           'arbitrary_function': arbitrary_function,
#                                           'left_board': left_board,
#                                           'right_board': right_board,
#                                           'accuracy': accuracy,
#                                           'k_for_x_3': 0,
#                                           'k_for_x_2': 0,
#                                           'k_for_x_1': 0,
#                                           'k_for_constant': 0,
#                                       })