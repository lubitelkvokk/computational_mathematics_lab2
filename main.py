from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.controller.polynom_solver import router as polynom_solver_router
from src.controller.system_of_polynom_solver import router as polynom_system_solver_router
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(polynom_solver_router)
app.include_router(polynom_system_solver_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
