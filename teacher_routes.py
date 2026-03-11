from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from db_config import get_db
from response_models import TeacherCreate, TeacherResponse
from teacher_repository import TeacherRepository

router = APIRouter(prefix="/teachers", tags=["Teacher endpoints"])

@router.post("/",response_model=TeacherResponse,status_code=status.HTTP_201_CREATED)
async def create_teacher(data:TeacherCreate,db: AsyncSession= Depends(get_db)):
    repo = TeacherRepository(db)
    teacher = await repo.create(data)
    return teacher

@router.get("/{teacher_id}", response_model=TeacherResponse)
async def get_teacher_by_id(teacher_id: int, db: AsyncSession = Depends(get_db)):
    repo = TeacherRepository(db)
    teacher = await repo.get_by_id(teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.get("/{teacher_email}", response_model=TeacherResponse)
async def get_teacher_by_email(teacher_email: int, db: AsyncSession = Depends(get_db)):
    repo = TeacherRepository(db)
    teacher = await repo.get_by_id(teacher_email)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.get("/", response_model=List[TeacherResponse])
async def get_all_teacher(offset: int = 0,limit: int = 10,db: AsyncSession = Depends(get_db)):
    repo = TeacherRepository(db)
    teachers = await repo.get_all_teacher(offset=offset, limit=limit)
    return teachers

