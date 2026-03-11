from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from response_models import CoursesCreate
from db_models import Courses, enrollment, Student


class CourseRepository:

    def __init__(self, db: AsyncSession):
        self.db = db
    async def get_student(self,student_ids : List[int]):
        query = select(Student).where(Student.id.in_(student_ids))
        result = await self.db.execute(query)
        return  list(result.scalars().all())

    async def create(self, data: CoursesCreate) -> Courses:
        course = Courses(teacher_id = data.teacher_id , name = data.name, code =data.code,destiption =data.description,credits = data.credit,is_active =data.is_active)

        self.db.add(course)
        await self.db.commit()
        await self.db.refresh(course)
        return course




