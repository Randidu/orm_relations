from fastapi import FastAPI
from teacher_routes import router as teacher_routes

app = FastAPI(
    title="CClarke ORM Implementation with DB Agent"
)


app.include_router(teacher_routes)