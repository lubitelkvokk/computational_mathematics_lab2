from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from src.service.polynom_solver_service import solve_with_chords, solve_with_newton, solve_with_simple_iteration
from src.service.polynom_system_service import solve_first_system, solve_second_system
from src.util.function_parser import create_lambda_function
from src.util.plot_generator import generate_plot

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/solve_system")
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
    return templates.TemplateResponse("polynom_system.html", default_values)


@router.post("/solve_system")
async def plot_graph_by_polynom_system(request: Request, x0: float = Form(...), y0: float = Form(...),
                                       accuracy: float = Form(...), system_choice: str = Form(...)):
    plot_data = ""
    try:

        if (system_choice == "system1"):
            result = solve_first_system(x0, y0, accuracy)
            plot_data = "static/images/system1.png"
        elif (system_choice == "system2"):
            result = solve_second_system(x0, y0, accuracy)
            plot_data = "static/images/system2.png"
    except Exception as e:
        result = e
    return templates.TemplateResponse("polynom_system.html",
                                      {
                                          "request": request,
                                          "result": result,
                                          "plot_data": plot_data
                                      })
