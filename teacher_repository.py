from typing import Any, Coroutine, Sequence
from sqlalchemy import select, Row, RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload
from db_models import TeacherProfile, Teacher
from response_models import TeacherCreate

class TeacherRepository:

    def __init__(self, db: AsyncSession):
        self.db = db


    async def create(self,data: TeacherCreate) -> Teacher:

        teacher = Teacher(name=data.name,email=data.email)

        if data.profile:
            teacher.profile = TeacherProfile(
                qualifications=data.profile.qualification,
                department=data.profile.department,
                office_number=data.profile.office_number,
                bio=data.profile.bio

            )
        self.db.add(teacher)
        await self.db.commit()
        await self.db.refresh(teacher)
        return teacher

    async def get_by_id(self, teacher_id: int) -> Teacher | None:
        query = (
            select(Teacher)
            .where(Teacher.id == teacher_id)
            .options(joinedload(Teacher.profile),
                     selectinload(Teacher.courses))   # eager load profile
        )
        result = await self.db.execute(query)
        return result.unique().scalars().first()

    async def get_all_teacher(self,offset:int =0,limit :int=10) -> Sequence[Teacher]:
        query = (select(Teacher).offset(offset).limit(limit))
        result = await self.db.execute(query)
        return list(result.scalars().all())

    async def get_by_email(self, teacher_email: str) -> Teacher | None:
        query = (
            select(Teacher)
            .where(Teacher.email == teacher_email)
            .options(joinedload(Teacher.profile),
                     selectinload(Teacher.courses))   # eager load profile
        )
        result = await self.db.execute(query)
        return result.unique().scalars().first()


