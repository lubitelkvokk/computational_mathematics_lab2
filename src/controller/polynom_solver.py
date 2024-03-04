from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from src.service.polynom_solver_service import solve_with_chords, solve_with_newton, solve_with_simple_iteration
from src.util.plot_generator import generate_plot

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/plot")
async def polynomial_solver(request: Request):
    return templates.TemplateResponse("polynom_solver.html", {"request": request})


@router.post("/plot")
async def plot_graph(request: Request, k_for_x_3: float = Form(...), k_for_x_2: float = Form(...),
                     k_for_x_1: float = Form(...), k_for_constant: float = Form(...),
                     left_board: float = Form(...), right_board: float = Form(...),
                     accuracy: float = Form(...)):
    generate_plot(k_for_x_3, k_for_x_2, k_for_x_1, k_for_constant, left_board, right_board, accuracy)

    # Возврат изображения графика как HTTP-ответ
    # result = solve_with_chords(left_board, right_board,
    #                            [k_for_constant, k_for_x_1, k_for_x_2, k_for_x_3],
    #                            accuracy)

    try:
        result = solve_with_simple_iteration(left_board, right_board,
                                   [k_for_constant, k_for_x_1, k_for_x_2, k_for_x_3],
                                   accuracy)
    except Exception as e:
        result = e
    print(result)
    return templates.TemplateResponse("polynom_solver.html",
                                      {"request": request, "plot_data": "static/images/image.png", "result": result})
