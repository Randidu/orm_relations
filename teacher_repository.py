from sqlalchemy.ext.asyncio import AsyncSession

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