from fastapi import APIRouter, Depends
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