from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db_config import get_db
from response_models import StudentCreate, StudentResponse
from student_repository import StudentRepository

router = APIRouter(prefix="/Students", tags=["Student endpoints"])

@router.post("/",response_model=StudentResponse,status_code=status.HTTP_201_CREATED)
async def create_Student(data:StudentCreate,db: AsyncSession= Depends(get_db)):
    repo = StudentRepository(db)
    student = await repo.create(data)
    return student



